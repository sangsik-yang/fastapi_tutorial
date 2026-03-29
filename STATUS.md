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
- **Comment System (NEW)**: 답변에 대한 댓글 작성, 조회, 삭제 기능 완료
- **Search System**: 통합 검색 기능 완료
- **Tag System**: 질문-태그 연동 및 인라인 태그 UI 완료
- **Infrastructure**:
    - CORS 설정 (`localhost:5173`, `127.0.0.1:5173`) 완료
    - Alembic 마이그레이션 및 DB 스키마 최신화 완료 (Comment 테이블 포함)

## 4. Known Issues & Notes
- Pydantic v2 마이그레이션 완료: `from_attributes = True`를 적용하여 ORM 모델 호환성 및 성능을 최적화했습니다.
- 서버 실행 시 가상환경(`.venv`)의 바이너리를 직접 사용하는 것이 안정적임
