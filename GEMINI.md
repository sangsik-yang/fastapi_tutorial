# FastAPI Tutorial Project - Gemini Context

이 파일은 Gemini CLI가 이 프로젝트에서 수행한 작업 내역과 해결된 주요 이슈들을 기록한 문서입니다.

## 👤 사용자 정보
- **이름**: 상식 (Sangsik-Yang)

## 🚀 주요 성공 사례 및 구현 내역 (2026-03-21 세션)

### 1. 태그 시스템 (Tag System) 완결
- **인라인 태그 생성**: 질문 등록 및 수정 화면에서 별도의 페이지 이동 없이 즉석에서 태그를 생성하고 선택할 수 있는 UI/UX를 구현했습니다.
- **안정적인 상태 관리**: Svelte의 `Set` 객체와 반응형(reactive) 문법을 활용하여, 태그 목록이 갱신되어도 사용자의 선택 상태가 유지되도록 로직을 개선했습니다.
- **전방위적 UI 반영**: 메인 질문 목록(Home), 질문 상세(Detail), 등록/수정(Create/Modify) 모든 곳에 태그 표시 및 연동을 완료했습니다.

### 2. 데이터베이스 및 마이그레이션 이슈 해결
- **Alembic 헤드 병합**: 마이그레이션 이력이 여러 갈래(Multiple Heads)로 나뉘어 충돌하던 문제를 `alembic merge`를 통해 해결했습니다.
- **스키마 동기화**: 누락되었던 `tag` 및 `question_tag` 테이블을 `alembic upgrade head`로 생성하고, `alembic stamp head`를 통해 DB 상태를 강제 동기화하여 `OperationalError`를 해결했습니다.

### 3. 백엔드-프론트엔드 연동 최적화
- **CORS 설정 수정**: `main.py`의 `origins` 목록에 프론트엔드 개발 서버(`localhost:5173`)를 추가하여 브라우저 차단 문제를 해결했습니다.
- **API 응답 개선**: 태그 생성 API가 생성된 객체를 즉시 반환(201 Created)하도록 하여 프론트엔드와 실시간으로 동기화되게 했습니다.
- **Svelte Store 접근 수정**: `$store` 문법을 사용하여 비표준적인 `.get()` 호출로 인한 런타임 에러를 해결했습니다.

## 🛠️ 개발 지침 (Project Standards)
- **가상환경**: `.venv` 내의 `python` 및 `uvicorn`을 명시적으로 사용해야 합니다.
- **Pydantic v2**: `orm_mode = True` 대신 `from_attributes = True` 권장 경고가 발생하므로 향후 리팩토링 시 참고합니다.
- **API 응답**: 모든 성공적인 JSON 응답은 `api.js`의 콜백을 통해 프론트엔드 상태로 즉시 반영되어야 합니다.

---
*이 문서는 프로젝트의 맥락을 유지하기 위해 Gemini에 의해 작성되었습니다.*
