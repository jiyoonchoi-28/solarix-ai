# Solarix AI — 랜딩 페이지

2026 Agentic AI Innovation Challenge 발표용 정적 소개 페이지입니다. CSS/JS가 모두 `index.html` 한 파일 안에 인라인되어 있어 외부 파일 의존성이 전혀 없고, 빌드 과정 없이 Render Static Site로 바로 배포할 수 있습니다.

## 로컬에서 확인하기

`index.html`을 더블클릭해서 브라우저로 바로 열면 됩니다. 외부 CSS/JS 파일을 불러오지 않는 단일 파일이라, OneDrive 동기화 상태나 상대경로 문제와 무관하게 항상 동일하게 렌더링됩니다.

정적 서버로 띄우고 싶다면:

```bash
npx serve .
```

## Render 배포 방법

### 방법 A — Blueprint(render.yaml) 사용
1. 이 폴더를 GitHub 저장소로 push 합니다.
2. [Render 대시보드](https://dashboard.render.com) → **New** → **Blueprint** → 방금 push한 저장소 선택.
3. 저장소 루트의 `render.yaml`을 자동으로 인식해 Static Site가 생성됩니다.
4. **Apply** 클릭하면 배포가 시작되고, 완료 후 `https://solarix-ai-landing.onrender.com` 형태의 URL이 발급됩니다.

### 방법 B — Static Site 수동 생성
1. Render 대시보드 → **New** → **Static Site**.
2. GitHub 저장소를 연결합니다 (이 `solarix-ai` 폴더가 루트가 되도록 Root Directory를 지정).
3. Build Command는 비워두고, Publish Directory는 `.` (현재 폴더)로 설정합니다.
4. **Create Static Site**를 누르면 배포가 진행됩니다.

## 폴더 구조

```
solarix-ai/
├── index.html   # 페이지 전체 (HTML + CSS + JS 인라인, 단일 파일)
└── render.yaml  # Render Blueprint 배포 설정
```
