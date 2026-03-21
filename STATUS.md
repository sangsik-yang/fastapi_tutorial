# Project Status & Architecture Overview

## 1. Tech Stack
- **Backend**: FastAPI, Python (Pydantic v2, SQLAlchemy 2.0)
- **Database**: SQLite (`myapi.db`), Alembic (Migrations)
- **Frontend**: Svelte (v5), Vite, JavaScript, Bootstrap 5
- **Authentication**: JWT-based (jose, passlib/Argon2)

## 2. Architecture & Directory Structure
- **Backend (DDD)**: `domain/` 하위에 `user`, `question`, `answer`, `tag` 도메인 별로 schema, crud, router 분리
- **Frontend**: `routes/` 기반 컴포넌트 라우팅 및 Svelte Store를 통한 전역 상태 관리

## 3. Current Implementation Status
- **User Management**: 회원가입, 로그인 (JWT) 완료
- **Q&A System**: 질문/답변 CRUD, 추천(Vote) 기능 완료
- **Search System**: 제목, 내용, 글쓴이, 답변 내용을 포함한 통합 검색 기능 완료
- **Tag System (NEW)**: 
    - 태그 생성, 목록 조회, 질문-태그 연동 기능 완료
    - 질문 등록/수정 시 실시간 태그 추가 및 다중 선택 UI 적용
- **Infrastructure**:
    - CORS 설정 (`localhost:5173`, `127.0.0.1:5173`) 완료
    - Alembic 마이그레이션 헤드 병합 및 DB 스키마 최신화 완료

## 4. Known Issues & Notes
- Pydantic v2 사용으로 인해 `orm_mode = True`에 대한 경고 발생 (향후 `from_attributes = True`로 리팩토링 권장)
- 서버 실행 시 가상환경(`.venv`)의 바이너리를 직접 사용하는 것이 안정적임
