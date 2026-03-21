import { writable } from 'svelte/store'

// Tag 목록을 저장하는 store
export const tag_list = writable([])

// 초기 값 설정
export function init_tag_list() {
    tag_list.set([])
}