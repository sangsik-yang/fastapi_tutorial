<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"
    import { tag_list } from '../lib/store/tag'

    export let params = {}
    const question_id = params.question_id

    let error = {detail: []}
    let subject = ''
    let content = ''
    let new_tag_name = ''
    let selected_tag_ids = new Set()

    function get_tag_list() {
        fastapi('get', '/api/tag/list', {}, (json) => {
            tag_list.set(json.tag_list || [])
        })
    }
    get_tag_list()

    function create_tag() {
        if (!new_tag_name.trim()) return
        fastapi('post', '/api/tag/create', {name: new_tag_name}, (json) => {
            new_tag_name = ''
            selected_tag_ids.add(json.id)
            selected_tag_ids = selected_tag_ids // trigger reactivity
            get_tag_list()
        })
    }

    fastapi("get", "/api/question/detail/"+question_id, {},(json)=>{
        subject = json.subject
        content = json.content
        if(json.tags) {
            selected_tag_ids = new Set(json.tags.map(t => t.id))
        }
    })

    $: all_tags = ($tag_list || []).map(tag => ({
        id: tag.id,
        name: tag.name,
        checked: selected_tag_ids.has(tag.id)
    }))

    function toggle_tag(id) {
        if (selected_tag_ids.has(id)) {
            selected_tag_ids.delete(id)
        } else {
            selected_tag_ids.add(id)
        }
        selected_tag_ids = selected_tag_ids // trigger reactivity
    }

    function update_question(event) {
        event.preventDefault()
        let url="/api/question/update"
        let params = {
            question_id: question_id,
            subject: subject,
            content: content,
            tag_ids: Array.from(selected_tag_ids),
        }
        fastapi('put', url, params, 
            (json) => {
                push('/detail/'+question_id)
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 수정</h5>
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="subject">제목</label>
            <input type="text" id="subject" class="form-control" bind:value="{subject}">
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea id="content" class="form-control" rows="10" bind:value="{content}"></textarea>
        </div>

        <div class="mb-3">
            <label class="fw-bold">태그 선택:</label>
            <div class="input-group mb-2" style="max-width: 300px;">
                <input type="text" class="form-control form-control-sm" placeholder="새 태그 이름" bind:value={new_tag_name} on:keydown={(e) => e.key === 'Enter' && (e.preventDefault(), create_tag())}>
                <button class="btn btn-outline-secondary btn-sm" type="button" on:click={create_tag}>추가</button>
            </div>
            {#if all_tags.length === 0}
                <div class="alert alert-info py-2">태그를 생성해주세요.</div>
            {:else}
                {#each all_tags as tag}
                    <label class="form-check form-check-inline mb-2">
                        <input 
                            type="checkbox" 
                            class="form-check-input" 
                            checked={tag.checked}
                            on:change={() => toggle_tag(tag.id)}
                        />
                        {tag.name}
                    </label>
                {/each}
            {/if}
        </div>

        <button class="btn btn-primary" on:click="{update_question}">수정하기</button>
    </form>
</div>