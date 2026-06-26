# Data

웹 구현에 필요한 최종 산출 데이터는 `processed/`에 있습니다.

이 폴더는 분석 원본을 모두 담은 곳이 아니라, 홈페이지 제작과 결과 검수에 바로 쓸 수 있게 정리한 데이터 폴더입니다. 처음 보는 사람은 파일을 하나씩 열기보다 아래 순서대로 보면 이해하기 쉽습니다.

## 추천 사용 순서

1. `processed/web_payload.json`
2. `processed/policy_alignment_status.csv`
3. `processed/plot_series.csv`
4. `processed/sector_recipe.csv`

각 파일의 역할은 다릅니다.

| 순서 | 파일 | 먼저 보는 이유 |
| ---: | --- | --- |
| 1 | `processed/web_payload.json` | 홈페이지에서 필요한 데이터를 한 번에 불러올 수 있습니다. |
| 2 | `processed/policy_alignment_status.csv` | 정책 카드에 들어갈 정책명, 섹터, r, 정합 등급, 기사 수를 표로 확인할 수 있습니다. |
| 3 | `processed/plot_series.csv` | 정책 상세 차트에 들어갈 날짜별 NLP/CAR 값을 확인할 수 있습니다. |
| 4 | `processed/sector_recipe.csv` | 섹터별 신호명과 lag 기준을 확인할 수 있습니다. |

CSV는 검수와 수동 확인용, JSON은 프론트엔드 로딩용으로 사용하면 됩니다. 예를 들어 기획자가 엑셀로 정책별 수치를 확인할 때는 CSV가 편하고, 개발자가 웹 화면을 만들 때는 JSON이 편합니다.

## 파일 목록

| 파일 | 설명 |
| --- | --- |
| `processed/web_payload.json` | 웹 통합 데이터입니다. 정책 카드, 섹터 기준, 차트 데이터를 한 파일에서 가져올 수 있습니다. |
| `processed/policy_alignment_status.csv/json` | 정책별 정합 판정 데이터입니다. 카드와 요약표의 기준입니다. |
| `processed/policy_alignment.csv/json` | 정책별 정합 계산 메타입니다. 어떤 신호와 주식그룹이 선택됐는지 확인할 때 씁니다. |
| `processed/sector_recipe.csv/json` | 섹터별 NLP 신호 기준입니다. 섹터 탭, 범례, 방법론 설명에 씁니다. |
| `processed/plot_series.csv/json` | 정책별 NLP/CAR 차트 시계열입니다. 정책 상세 라인 차트를 그릴 때 씁니다. |

자세한 컬럼 설명은 [`../docs/data-dictionary.md`](../docs/data-dictionary.md)를 확인하세요.

## 가장 흔한 사용 예

정책 카드 목록을 만들 때는 `policy_alignment_status`를 사용합니다.

```text
P08 K칩스법 1차
반도체 · LLM 시장반응 신호 · lag 0일
방향 정합 · 강한 정합 · r=0.942
선택 주식그룹: KOSDAQ·대기업
기사수: 2,232
```

정책 상세 차트를 만들 때는 `plot_series`를 사용합니다. 같은 `policy_n` 안에서 `kind`가 `nlp`인 값은 뉴스 흐름, `kind`가 `car`인 값은 주식 초과수익 흐름입니다.

낮은 r 정책은 `방향 정합`만 보고 강하게 표현하면 안 됩니다. `alignment_grade`가 `약한 정합`이면 화면에서도 낮은 강도 배지를 같이 보여주세요.
