# Reproducibility

이 저장소는 홈페이지 구현용 최종 산출 데이터 패키지입니다. 원자료 전체와 내부 분석 스크립트는 포함하지 않습니다.

## 포함된 산출물

- 정책별 정합 판정 CSV/JSON
- 정책별 정합 메타 CSV/JSON
- 섹터별 분석 기준 CSV/JSON
- 차트 시계열 CSV/JSON
- 웹 통합 payload JSON
- 제출용 보고서 DOCX/MD
- 결과 설명용 PNG 그림
- 기존 HTML 참고본

## 로컬 검증

```bash
python3 scripts/validate_data.py
```

확인 항목:

- 필수 파일 존재 여부
- 정책 수 50개
- 섹터 수 5개
- 정책별 정합 판정 50행
- 차트 시계열 7,139행
- `web_payload.json`의 필수 키

## 원자료 범위

원자료는 기사 원문, LLM 점수 산출 전 데이터, 시장 수익률 원자료 등을 포함합니다. 이 저장소에는 저작권, 계약, 재현 경로 관리를 위해 최종 웹 구현에 필요한 파생 산출물만 포함했습니다.

## 보고서 기준

최종 대외 제출용 보고서는 [`reports/seoul_economic_policy_news_external_report.docx`](../reports/seoul_economic_policy_news_external_report.docx)입니다.

