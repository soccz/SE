# Data Dictionary

모든 웹 제작용 데이터는 [`data/processed/`](../data/processed/)에 있습니다.

## `web_payload.json`

프론트엔드에서 가장 먼저 확인할 통합 payload입니다.

| 키 | 타입 | 설명 |
| --- | --- | --- |
| `meta` | object | 프로젝트명, 버전, 정책 수, 섹터 수 |
| `sector_recipe` | array | 섹터별 NLP 신호 기준 |
| `policy_alignment` | array | 정책별 정합 계산 메타 |
| `policy_alignment_status` | array | 정책별 정합 판정 카드용 데이터 |
| `plot_series` | array | 정책별 NLP/CAR 라인 차트 시계열 |

## `policy_alignment_status.csv/json`

정책 카드와 정책별 정합 판정표의 기준 데이터입니다.

| 컬럼 | 타입 | 설명 |
| --- | --- | --- |
| `policy_n` | integer | 정책 번호 |
| `policy_code` | string | `P01` 형식 정책 코드 |
| `policy_name` | string | 정책명 |
| `sector` | string | 섹터명 |
| `display_label` | string | 대외 표기용 NLP 신호명 |
| `source` | string | 웹/API용 신호 코드 |
| `lag` | integer | 섹터별 반응 지연일 |
| `best_group` | string | 정합 기준으로 선택된 주식그룹 |
| `r` | number | NLP 누적흐름과 CAR의 정합 상관계수 |
| `alignment_status` | string | 정합 판정 |
| `alignment_grade` | string | r 기준 정합 등급 |
| `n_ptei` | integer | 정책별 기사 수 |

## `policy_alignment.csv/json`

분석 계산값에 가까운 정책별 메타입니다.

| 컬럼 | 설명 |
| --- | --- |
| `policy_n` | 정책 번호 |
| `sector` | 섹터명 |
| `source` | 대외 변환된 NLP 신호 코드 |
| `span` | 일별 신호 산출 단위 |
| `sign` | 적용 방향. 대외 산출물은 전 정책 `+1` |
| `lag` | 섹터별 반응 지연일 |
| `best_group` | 선택 주식그룹 |
| `r` | 정합 상관계수 |
| `mode` | 정합 모드 |
| `n_ptei` | 기사 수 |
| `display_label` | 대외 표기용 신호명 |

## `sector_recipe.csv/json`

섹터별 탭, 범례, 방법론 설명에 사용합니다.

| 컬럼 | 설명 |
| --- | --- |
| `sector` | 섹터명 |
| `source` | 웹/API용 신호 코드 |
| `label` | 대외 표기용 NLP 신호명 |
| `span` | 신호 산출 단위 |
| `lag` | 섹터 공통 반응 지연일 |
| `n_policy` | 섹터 내 정책 수 |
| `display_label` | UI 표시명 |

## `plot_series.csv/json`

정책 상세 라인 차트 데이터입니다.

| 컬럼 | 설명 |
| --- | --- |
| `policy_n` | 정책 번호 |
| `kind` | `nlp` 또는 `car` |
| `cal_day` | 정책일 D0 기준 상대일 |
| `value` | 차트 값 |

프론트엔드에서는 `policy_n`과 `kind`로 필터링한 뒤 `cal_day` 기준으로 정렬하면 됩니다.

