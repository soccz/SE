# Data

웹 구현에 필요한 최종 산출 데이터는 `processed/`에 있습니다.

## 추천 사용 순서

1. `processed/web_payload.json`
2. `processed/policy_alignment_status.csv`
3. `processed/plot_series.csv`
4. `processed/sector_recipe.csv`

CSV는 검수와 수동 확인용, JSON은 프론트엔드 로딩용으로 사용하면 됩니다.

## 파일 목록

| 파일 | 설명 |
| --- | --- |
| `processed/web_payload.json` | 웹 통합 payload |
| `processed/policy_alignment_status.csv/json` | 정책별 정합 판정 |
| `processed/policy_alignment.csv/json` | 정책별 정합 계산 메타 |
| `processed/sector_recipe.csv/json` | 섹터별 NLP 신호 기준 |
| `processed/plot_series.csv/json` | 정책별 NLP/CAR 차트 시계열 |

자세한 컬럼 설명은 [`../docs/data-dictionary.md`](../docs/data-dictionary.md)를 확인하세요.

