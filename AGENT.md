# FastAPI Tutorial Project - Agent Guide

## 프로젝트 개요
- **Tech Stack**: FastAPI, SQLAlchemy, Svelte (프론트엔드)
- **목표**: Q&A 기반 지식 공유 플랫폼 구축

## 데이터 모델

### Entity 관계
```
User ──(1:N)── Question ──(M:M)── Tag
  │                 │
  │               (1:N)
  │                 │
  └────(1:N)─────── Answer
```

### 테이블 구조
- `user`: 사용자 정보 (id, username, password, email)
- `question`: 질문 (id, subject, content, create_date, user_id, tags)
- `answer`: 답변 (id, content, create_date, question_id, user_id)
- `tag`: 태그 (id, name)
- `question_tag`: 질문-태그 다대다 관계 테이블

## 구현된 핵심 기능
✅ **Question & Search**: 제목/내용/작성자/답변 기반 검색 필터링  
✅ **Tag System**: 
- 인라인 태그 생성 API 및 UI
- 질문 등록/수정 시 동적 태그 연동
- 질문 목록 및 상세 페이지 태그 표시 배지 적용
✅ **Infrastructure**:
- CORS 허용 설정 (Dev Server 지원)
- Alembic 마이그레이션 이력 관리 및 병합 완료

## 주요 가이드라인
- **Backend**: `domain/` 구조를 엄격히 따르며, 새로운 기능을 추가할 때는 `schema` -> `crud` -> `router` 순으로 구현합니다.
- **Frontend**: `api.js`의 `fastapi` 헬퍼를 사용하여 백엔드와 통신하며, 상태는 `$tag_list`와 같은 Store를 활용합니다.
- **DB**: 모델 변경 시 반드시 `alembic revision --autogenerate` 후 `upgrade head`를 실행합니다.

## 환경 설정
```bash
# 백엔드 실행
./.venv/bin/uvicorn main:app --reload --port 8000 --host 127.0.0.1

# 프론트엔드 실행
npm run dev --prefix frontend
```
