# While-True

## 🚀 스터디 소개

**While-True**는 **멈추지 않고 꾸준히 학습을 이어가자**는 의미를 담은 알고리즘 스터디입니다.

단순히 문제를 푸는 데서 끝나는 것이 아니라,

- 왜 이렇게 풀었는지
- 어디서 막혔는지
- 어떻게 개선할 수 있는지

를 **기록하고 공유하며 함께 성장하는 것**을 목표로 합니다.

## 🛠️ 참여 가이드

### 1️⃣ Clone Repository

- 저장소를 로컬 환경으로 clone 합니다.
- contributor로 지정되기 때문에, 본인의 GitHub 계정에서 바로 확인할 수 있습니다.

---

### 2️⃣ branch 생성 및 이동

- 문제 풀이는 반드시 **개인 branch**에서 진행합니다.
- 브랜치 이름 규칙 : `이름 이니셜-solve`

  ```bash
  git switch -c pjw-solve
  ```

---

### 3️⃣ 문제 풀이

```txt
1월_2주차/
├── 1월_2주차.md
├── baekjoon-1002/
│   └── pjw-solve.py
├── baekjoon-1004/
│   └── pjw-solve.py

```

- 주차별 md 파일에서 문제를 확인합니다.
- 문제 번호별 폴더 안에 **본인 이니셜 파일명으로 풀이 파일을 생성**하여 작성합니다.

---

### 4️⃣ commit & push

```bash
git add .
git commit -m "풀이 날짜"
git push origin <branch명>
```

---

### 5️⃣ Pull Request 작성

GitHub에서 PR을 생성합니다. 아래 내용을 간단히 작성해주세요.

- 풀이 접근 방법
- 고민했던 부분
- 새롭게 배운 점
- 개선 사항

이후, 다른 사람들의 PR에 리뷰를 달아주세요.
