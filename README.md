# FastAPI & Svelte Q&A 플랫폼

이 프로젝트는 **FastAPI**와 **Svelte**를 활용하여 구축된 Q&A 기반의 지식 공유 플랫폼입니다.
사용자 간의 질문과 답변, 추천 기능, 그리고 강력한 태그 시스템을 제공합니다.

## 🚀 주요 기능

### 1. 질문 및 답변 (Q&A)
- 질문 작성, 수정, 삭제 및 상세 조회
- 답변 작성, 수정, 삭제 기능
- 질문과 답변에 대한 추천(Vote) 시스템

### 2. 강력한 검색 기능
- 제목, 내용, 작성자, 답변 내용 등을 포함한 통합 검색 지원

### 3. 지능형 태그 시스템 (New!)
- 질문 등록 및 수정 시 **인라인 태그 생성** 기능 제공
- 질문 목록 및 상세 페이지에서 태그 시각화 (Badge)
- 다대다(M:M) 관계 기반의 효율적인 태그 연동

### 4. 사용자 관리
- JWT 기반의 안전한 회원가입 및 로그인 시스템

## 🛠️ 기술 스택

- **Backend**: FastAPI, SQLAlchemy (ORM), Alembic (Migration), Pydantic v2
- **Database**: SQLite
- **Frontend**: Svelte (v5), Vite, Bootstrap 5
- **Auth**: JWT (OAuth2 Password Bearer)

## ⚙️ 설치 및 실행 방법

### 백엔드 (FastAPI)
1. 가상환경 생성 및 활성화
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. 의존성 설치
   ```bash
   pip install -r requirements.txt
   ```
3. 데이터베이스 초기화 및 마이그레이션
   ```bash
   alembic upgrade head
   ```
4. 서버 실행
   ```bash
   uvicorn main:app --reload --port 8000 --host 127.0.0.1
   ```

### 프론트엔드 (Svelte)
1. 프론트엔드 디렉토리 이동 및 패키지 설치
   ```bash
   cd frontend
   npm install
   ```
2. 개발 서버 실행
   ```bash
   npm run dev
   ```

## 📄 라이선스
이 프로젝트는 교육 및 포트폴리오 목적으로 제작되었습니다.
