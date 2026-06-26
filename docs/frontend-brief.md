# Frontend Brief

이 문서는 인터랙티브 홈페이지 제작자를 위한 구현 가이드입니다.

## 참고 방향

- 참고 저장소: <https://github.com/whchoi98/ontology-for-assembly>
- 참고 사이트: <https://assembly.whchoi.net/>

참고 사이트처럼 좌측 탐색 또는 상단 탭, KPI 카드, 시나리오 카드, 상세 패널을 조합하는 구조가 잘 맞습니다. 이 프로젝트에서는 “시나리오”를 섹터와 정책 카드로 치환하면 됩니다.

## 권장 정보 구조

```text
Home
├── KPI summary
├── Sector tabs
│   ├── 반도체
│   ├── 금융/증권
│   ├── 바이오/제약
│   ├── 부동산/건설
│   └── 2차전지/에너지
├── Policy card grid
├── Policy detail chart
├── Methodology
└── Data download
```

## 첫 화면 KPI

| KPI | 값 |
| --- | --- |
| 정책 | 50건 |
| 뉴스 | 121,954건 |
| 섹터 | 5개 |
| 평균 정합 | r=0.706 |
| 방향 정합 | 50/50 |
| 강한·높은 정합 | 38/50 |

## 정책 카드 필드

`policy_alignment_status`를 사용합니다.

- `policy_code`
- `policy_name`
- `sector`
- `display_label`
- `lag`
- `best_group`
- `r`
- `alignment_status`
- `alignment_grade`
- `n_ptei`

권장 카드 문구:

```text
P08 K칩스법 1차
반도체 · LLM 시장반응 신호 · lag 0일
방향 정합 · 강한 정합 · r=0.942
선택 주식그룹: KOSDAQ·대기업
기사수: 2,232
```

`r < 0.4` 정책은 방향 정합은 표시하되, 강한 성과 카드처럼 보이지 않게 `약한 정합` 배지로 구분하세요.

## 초심자용 문구와 툴팁

홈페이지에는 데이터 분석에 익숙하지 않은 독자를 위해 짧은 도움말을 붙이는 것을 권장합니다.

| 위치 | 문구 |
| --- | --- |
| `r` 툴팁 | 뉴스 흐름과 주가 흐름이 얼마나 비슷하게 움직였는지를 나타내는 값입니다. 1에 가까울수록 강합니다. |
| `방향 정합` 툴팁 | 두 흐름이 같은 방향으로 잡혔다는 뜻입니다. 정합 강도는 r 등급을 함께 봐야 합니다. |
| `약한 정합` 툴팁 | 방향은 같지만 r 값이 낮아 강한 사례로 볼 수 없습니다. |
| `CAR` 툴팁 | 시장 전체 움직임을 뺀 관련 주식그룹의 누적 초과수익입니다. |
| `lag` 툴팁 | 뉴스 흐름과 주가 흐름을 비교할 때 적용한 시간 간격입니다. |

처음 보는 독자에게는 `정책별 방향 정합 50/50`과 `강한·높은 정합 38/50`을 함께 보여주세요. 이렇게 해야 “모든 정책이 강하게 맞았다”는 오해를 줄일 수 있습니다.

## 상세 차트

`plot_series`를 사용합니다.

1. 선택된 `policy_n`으로 필터링
2. `kind === "nlp"`와 `kind === "car"`를 분리
3. `cal_day`를 x축으로 정렬
4. 이중축 라인 차트로 표시

권장 범례:

- 파란 선: NLP 누적흐름
- 빨간 선: 정책주 초과수익 CAR
- x축: 정책일 D0 기준 상대일

## 색상 제안

기존 결과 그림의 섹터 팔레트를 기준으로 합니다.

| 섹터 | 색상 |
| --- | --- |
| 반도체 | `#2f73bd` |
| 금융/증권 | `#2a927e` |
| 바이오/제약 | `#8a63c3` |
| 부동산/건설 | `#bf6b16` |
| 2차전지/에너지 | `#c74335` |

## 데이터 로딩 예시

```ts
type PlotPoint = {
  policy_n: number;
  kind: "nlp" | "car";
  cal_day: number;
  value: number;
};

const payload = await fetch("/data/processed/web_payload.json").then((res) => res.json());
const policy = payload.policy_alignment_status.find((row) => row.policy_code === "P08");
const series = payload.plot_series
  .filter((row: PlotPoint) => row.policy_n === policy.policy_n)
  .sort((a: PlotPoint, b: PlotPoint) => a.cal_day - b.cal_day);
```

## 다운로드 섹션

홈페이지 하단에는 아래 링크를 제공하면 제작/검수에 좋습니다.

- `web_payload.json`
- `policy_alignment_status.csv`
- `plot_series.csv`
- 제출용 보고서 DOCX
