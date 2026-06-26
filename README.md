# Seoul Economic Policy News Dataset

서울경제 「정책 뉴스의 힘 - 50대 정책」 인터랙티브 페이지 제작을 위한 공개용 결과 패키지입니다.

이 저장소는 프론트엔드 애플리케이션 자체가 아니라, 홈페이지 제작자가 바로 사용할 수 있는 데이터, 분석 방법, 결과 요약, 시각화 설계 지침을 제공합니다. 구성 방향은 [`whchoi98/ontology-for-assembly`](https://github.com/whchoi98/ontology-for-assembly)와 데모 사이트 [`assembly.whchoi.net`](https://assembly.whchoi.net/)처럼 데이터 중심 프로젝트를 README와 문서로 설명하고, 웹 화면은 카드/탭/상세 패널로 확장할 수 있게 하는 방식입니다.

## 핵심 메시지

- 정책 50건을 5개 섹터로 분류하고, 섹터별 10개 정책을 동일한 형식으로 정리했습니다.
- 정책 관련 뉴스 121,954건을 활용했고, LLM 점수 가용 기사 118,602건을 분석했습니다.
- 정책별 NLP 흐름과 정책주 초과수익 CAR의 방향 정합은 50개 정책 모두에서 확인됩니다.
- 평균 정합 상관계수는 `r = 0.706`입니다.
- 다만 P33, P36, P46, P50처럼 `r < 0.4`인 정책은 방향은 같지만 정합 강도는 약한 사례로 분리 표시합니다.
- 웹 구현에 필요한 핵심 데이터는 `data/processed/web_payload.json` 하나로도 로드할 수 있습니다.

## 처음 보는 사람을 위한 5분 요약

이 프로젝트는 “정책 뉴스가 나온 뒤, 그 뉴스의 분위기와 관련 주식 움직임이 비슷한 흐름을 보였는가?”를 정리한 자료입니다.

쉽게 말하면 다음 순서입니다. 아래 6단계만 이해해도 전체 보고서의 큰 그림을 잡을 수 있습니다.

1. 먼저 50개 경제정책을 고릅니다.
2. 각 정책 전후의 관련 뉴스를 모읍니다.
3. 뉴스가 시장에 긍정적으로 읽히는지, 정책을 수용하는 분위기인지 등을 NLP 점수로 바꿉니다.
4. 같은 기간 관련 주식그룹의 초과수익 흐름을 계산합니다.
5. 뉴스 흐름과 주가 흐름이 얼마나 비슷하게 움직였는지 `r` 값으로 표시합니다.
6. 홈페이지에서는 각 정책을 카드로 보여주고, 상세 화면에서는 뉴스 흐름과 CAR 차트를 같이 보여주면 됩니다.

이 저장소의 핵심은 “결론만 보여주는 자료”가 아니라 “홈페이지 제작자가 어떤 데이터를 어디에 써야 하는지 바로 알 수 있게 정리한 자료”입니다. 그래서 데이터 파일, 결과 요약, 방법론 설명, 화면 구성 가이드를 함께 넣어두었습니다.

핵심 용어를 아주 짧게 풀면 다음과 같습니다.

| 용어 | 쉬운 설명 |
| --- | --- |
| 정책 | 분석의 기준이 되는 이벤트입니다. 예: K칩스법, 8·31 대책, 그린뉴딜 |
| 섹터 | 정책이 주로 관련되는 산업 묶음입니다. 예: 반도체, 금융/증권 |
| NLP 신호 | 뉴스 문장을 컴퓨터가 읽을 수 있는 숫자로 바꾼 값입니다. 뉴스 분위기나 정책 수용 흐름을 뜻합니다. |
| LLM | 문장을 읽고 판단하는 대규모 언어모델입니다. 이 분석에서는 뉴스 반응을 점수화하는 데 쓰인 기준으로 이해하면 됩니다. |
| PTEI | 정책 수용 흐름을 나타내는 분석 신호명입니다. 홈페이지에서는 `PTEI 정책수용 신호`처럼 설명형 이름으로 보여주면 됩니다. |
| CAR | 시장 전체 흐름을 뺀 뒤 관련 주식이 누적으로 얼마나 움직였는지를 보는 값입니다. |
| r | 뉴스 흐름과 주가 흐름이 얼마나 비슷하게 움직였는지 나타내는 점수입니다. 1에 가까울수록 강합니다. |
| payload | 웹에서 한 번에 불러오기 좋게 여러 데이터를 묶어둔 JSON 파일입니다. |
| 방향 정합 | 두 흐름의 방향이 같은 쪽으로 잡혔다는 뜻입니다. 강도가 높다는 뜻은 아닙니다. |
| 약한 정합 | 방향은 같지만 `r`이 낮아 강한 사례로 말하면 안 되는 정책입니다. |

처음 읽는 사람은 [`docs/plain-language-guide.md`](docs/plain-language-guide.md)를 먼저 보면 됩니다. 보고서 용어, 정책 카드 읽는 법, 강한/약한 정합을 구분하는 방법을 쉬운 문장으로 정리했습니다.

## 처음 보는 사람이 읽는 순서

분석 경험이 없거나 프로젝트 배경을 모르는 사람은 아래 순서로 보면 됩니다.

| 순서 | 문서 | 먼저 봐야 하는 이유 |
| ---: | --- | --- |
| 1 | [`docs/plain-language-guide.md`](docs/plain-language-guide.md) | 정책, NLP, CAR, r, 정합 같은 용어를 쉬운 말로 풉니다. |
| 2 | [`docs/results-summary.md`](docs/results-summary.md) | 전체 결과가 어떤 숫자로 요약되는지 확인합니다. |
| 3 | [`docs/frontend-brief.md`](docs/frontend-brief.md) | 홈페이지 첫 화면, 정책 카드, 상세 차트에 무엇을 보여줄지 확인합니다. |
| 4 | [`docs/data-dictionary.md`](docs/data-dictionary.md) | 각 데이터 파일과 컬럼을 어떤 뜻으로 읽어야 하는지 확인합니다. |
| 5 | [`docs/methodology.md`](docs/methodology.md) | 분석이 어떤 순서로 수행됐는지 방법론을 확인합니다. |
| 6 | [`reports/seoul_economic_policy_news_external_report.docx`](reports/seoul_economic_policy_news_external_report.docx) | 제출용 보고서 본문과 그림을 확인합니다. |

이 저장소가 말하는 것은 “정책 뉴스 흐름과 관련 주식 흐름의 정합을 확인했다”입니다. 반대로 “뉴스가 주가를 반드시 예측했다”거나 “모든 정책이 강하게 맞았다”는 뜻은 아닙니다. 특히 `r < 0.4` 정책은 홈페이지에서 반드시 `약한 정합`으로 표시해야 합니다.

## 바로 쓰는 파일

| 목적 | 파일 |
| --- | --- |
| 웹 통합 payload | [`data/processed/web_payload.json`](data/processed/web_payload.json) |
| 정책별 정합 판정 | [`data/processed/policy_alignment_status.csv`](data/processed/policy_alignment_status.csv) |
| 정책별 정합 메타 | [`data/processed/policy_alignment.csv`](data/processed/policy_alignment.csv) |
| 차트 시계열 | [`data/processed/plot_series.csv`](data/processed/plot_series.csv) |
| 섹터별 분석 기준 | [`data/processed/sector_recipe.csv`](data/processed/sector_recipe.csv) |
| 결과 그림 | [`assets/figures/`](assets/figures/) |
| 제출용 보고서 | [`reports/seoul_economic_policy_news_external_report.docx`](reports/seoul_economic_policy_news_external_report.docx) |
| 기존 HTML 참고본 | [`reference/policy_nlp_car_demo.html`](reference/policy_nlp_car_demo.html) |

## 저장소 구조

```text
.
├── README.md
├── data/
│   ├── README.md
│   └── processed/
│       ├── web_payload.json
│       ├── policy_alignment_status.csv/json
│       ├── policy_alignment.csv/json
│       ├── sector_recipe.csv/json
│       └── plot_series.csv/json
├── docs/
│   ├── data-dictionary.md
│   ├── frontend-brief.md
│   ├── methodology.md
│   ├── plain-language-guide.md
│   ├── results-summary.md
│   └── reproducibility.md
├── assets/
│   ├── README.md
│   └── figures/
├── reports/
│   ├── README.md
│   └── seoul_economic_policy_news_external_report.docx
├── reference/
│   ├── README.md
│   └── policy_nlp_car_demo.html
└── scripts/
    └── validate_data.py
```

## 홈페이지 제작 방향

첫 화면은 `assembly.whchoi.net`처럼 좌측 탐색 또는 상단 탭으로 섹터를 나누고, 본문에는 KPI 카드와 정책 카드 목록을 배치하는 방식을 권장합니다.

권장 화면:

1. **Overview**: 정책 50건, 뉴스 121,954건, 평균 `r=0.706`, 방향 정합 50/50, 강한·높은 정합 38/50.
2. **Sector Tabs**: 반도체, 금융/증권, 바이오/제약, 부동산/건설, 2차전지/에너지.
3. **Policy Cards**: 정책명, 기준 신호, lag, 선택 주식그룹, 기사수, `r`, 정합 판정.
4. **Policy Detail**: NLP 누적흐름과 CAR 이중축 라인 차트.
5. **Methods**: 섹터별 NLP 기준, CAR 계산, 그레인저 선행성 검정 체계.

자세한 구현 지침은 [`docs/frontend-brief.md`](docs/frontend-brief.md)를 기준으로 보세요.

## 주요 결과

| 항목 | 값 |
| --- | ---: |
| 정책 수 | 50 |
| 섹터 수 | 5 |
| 뉴스 기사 수 | 121,954 |
| LLM 점수 가용 기사 수 | 118,602 |
| 정책별 방향 정합 | 50/50 |
| 평균 정합 r | 0.706 |
| 차트 시계열 행 수 | 7,139 |

섹터별 요약과 정책별 판정은 [`docs/results-summary.md`](docs/results-summary.md)를 확인하세요.

## 데이터 사용 순서

프론트엔드에서는 아래 순서로 연결하면 됩니다.

1. `web_payload.json` 로드
2. `sector_recipe`로 섹터 탭과 신호 설명 구성
3. `policy_alignment_status`로 정책 카드 구성. `alignment_status`는 방향 판정, `alignment_grade`는 r 기준 강도입니다.
4. `plot_series`에서 선택 정책의 `policy_n` 기준으로 `nlp`와 `car` 라인 분리
5. 상세 카드에 `policy_alignment`의 `best_group`, `lag`, `r` 표시

## 검증

```bash
python3 scripts/validate_data.py
```

검증 스크립트는 핵심 파일 존재 여부, 행 수, 정책 수, 섹터 수, `web_payload.json` 키 구조를 확인합니다.

## 주의

이 저장소에는 웹 제작에 필요한 최종 산출 데이터만 포함합니다. 기사 원문, 원천 주가 데이터, 내부 검토용 스크립트 및 계약 문서는 포함하지 않습니다.
