# SMAP 데이터 설명 
# SMAP Enhanced Level-3 Soil Moisture Data
## 1. 데이터 설명 
<details>
  <summary>1.1 파라미터 (Data Description)</summary>
  이 데이터 세트의 주요 출력은 표면 토양 습도입니다. 이는 대략적으로 토양 기둥 상단 5cm를 나타내며, m³/m³ 단위로 제공됩니다. 이 데이터는 9km EASE-Grid 2.0 투영에서 전 세계와 극지방 그리드로 표시됩니다.  
  데이터 필드는 전 세계와 극지방 그리드로 나뉘며, 각각 AM(오전), PM(오후)으로 구분된 HDF5 데이터 그룹에 저장됩니다.  
  극지방 그리드 투영은 높은 위도에서 더 균일한 공간 샘플링을 제공합니다.

  추가적으로, 밝기 온도(TB) 측정값도 포함됩니다. 이 값들은 SMAP의 향상된 Level-1B 밝기 온도로, 9km EASE2 그리드로 다시 샘플링된 값입니다.

  이 제품에는 세 가지 알고리즘이 포함되어 있습니다:
  - **이중 채널 알고리즘 (DCA)**
  - **단일 채널 알고리즘 - 수직 편광 (SCA-V)**
  - **단일 채널 알고리즘 - 수평 편광 (SCA-H)**

  버전 5부터 새로운 기본 알고리즘은 DCA입니다. 이전 버전에서는 SCA-V가 기본 알고리즘이었습니다. DCA는 일부 농업지에서 SCA-V보다 약간 더 나은 성능을 보여주었으나, 전체적인 성능은 유사합니다.
</details>

<details>
  <summary>1.2 파일 정보 (File Information)</summary>

  ### 1.2.1 형식
  데이터는 **HDF5** 형식으로 제공됩니다. HDF5 파일에 대한 소프트웨어와 자세한 내용은 HDF 그룹의 HDF5 웹사이트에서 확인할 수 있습니다.

  ### 1.2.2 파일 내용
  HDF5 파일은 메타데이터, AM/PM로 구분된 **토양 습도 데이터 그룹**, 그리고 극지방 AM/PM 데이터 그룹으로 구성됩니다. 각각의 그룹은 하위 데이터 세트 또는 그룹을 포함합니다.

  ### 1.2.3 데이터 필드
  각각 **토양 습도 데이터**, **보조 데이터**, 그리고 **품질 평가 플래그**를 포함합니다.  
  - **AM 그룹**: 위성을 북에서 남으로 통과할 때 데이터를 포함하며, 오전 6시 데이터를 수집합니다.  
  - **PM 그룹**: 남에서 북으로 통과할 때의 데이터를 포함하며, 오후 6시 데이터를 수집합니다.

  ### 1.2.4 메타데이터 필드
  이 그룹은 각 파일의 전체 내용을 설명하는 메타데이터를 포함합니다.

  ### 1.2.5 파일 네이밍 규칙
  파일명은 다음과 같은 규칙을 따릅니다:  
  `SMAP_L3_SM_P_E_yyyymmdd_RLVvvv_NNN.[확장자]`  
  예: `SMAP_L3_SM_P_E_20150403_R17400_001.h5`
</details>

<details>
  <summary>1.3 공간 정보 (Spatial Information)</summary>

  **1.3.1 범위 (Coverage)**  
  이 데이터의 글로벌 그리드 범위는 경도 180°W에서 180°E까지이며, 위도는 약 85.044°N에서 85.044°S까지입니다. 북극 그리드 범위는 북반구 전체, 즉 경도 180°W에서 180°E까지, 적도에서 90°N까지를 포함합니다.

  **1.3.2 해상도 (Resolution)**  
  SMAP 데이터의 기본 해상도는 약 36km이지만, 이 데이터는 Backus-Gilbert 최적 보간 알고리즘을 사용하여 9km 해상도로 보간되었습니다.

  **1.3.3 지리 정보 (Geolocation)**  
  이 데이터는 9km EASE-Grid 2.0 평등 면적 그리드를 기준으로 제공됩니다. 더 자세한 지리 정보는 EASE-Grid 웹사이트에서 확인할 수 있습니다.
</details>

<details>
  <summary>1.4 시간 정보 (Temporal Information)</summary>

  **1.4.1 범위 (Coverage)**  
  이 데이터의 시간 범위는 2015년 3월 31일부터 현재까지입니다.

  **1.4.2 위성 및 처리 이벤트 (Satellite and Processing Events)**  
  위성 기동, 데이터 다운링크 이상, 데이터 품질 필터링 등의 이유로 인해 SMAP 데이터 시리즈에 작은 간격이 발생할 수 있습니다. SMAP 위성이 안전 모드로 들어간 2019년 6월 19일부터 7월 23일까지 데이터 수집에 큰 공백이 있었습니다.

  **1.4.3 지연 시간 (Latencies)**  
  지연 시간에 대한 자세한 내용은 SMAP Radiometer 데이터 세트의 지연 시간에 대한 FAQ를 참고하세요.

  **1.4.4 해상도 (Resolution)**  
  각 Level-3 파일은 반 궤도 파일/스와스의 일일 합성본입니다. 하강 통과(a.m.) 및 상승 통과(p.m.)에서 수집된 데이터는 각각 동일한 일일 합성 파일에 별도로 저장됩니다.
</details>

## 2. DATA ACQUISITION AND PROCESSING

<details>
<summary>2.1 Background</summary>

전자기 스펙트럼의 마이크로파 영역(파장이 몇 센티미터에서 1미터까지 포함)은 원격으로 표면 토양 습도를 추정하는 데 가장 큰 가능성을 제공하는 것으로 오랫동안 알려져 왔습니다. 수동 마이크로파 센서는 지구 표면에서 방출되는 자연적인 열 방사를 측정합니다. 이 방사의 강도 변화는 목표 매질의 유전율과 온도에 따라 달라지며, 근표면 토양층의 경우 이는 습도의 양에 의해 결정됩니다. L-밴드 또는 약 1 GHz(20-30 cm)의 낮은 마이크로파 주파수(긴 파장)는 다음과 같은 이점을 제공합니다:

- 대기가 거의 완전히 투명하므로 모든 날씨에서 감지가 가능합니다.
- 드문드문한 식생층과 중간 정도의 식생층(최대 5 kg/m²의 식물 수분 함량을 포함) 아래에서 토양에서의 신호 전송이 가능합니다.
- 태양 광선의 영향을 받지 않으므로 낮과 밤 모두 관찰할 수 있습니다.

자세한 내용은 이 제품의 알고리즘 이론적 기초 문서(ATBD)의 2장을 참조하십시오(O'Neill et al., 2021a). 해당 문서는 기술 참조 자료로 제공됩니다.
</details>

<details>
<summary>2.2 Instrumentation</summary>

SMAP 계측기기에 대한 자세한 설명은 Jet Propulsion Laboratory(JPL) SMAP 웹사이트의 SMAP Instrument 페이지를 참조하세요.
</details>

<details>
<summary>2.3 Acquisition</summary>

SMAP 향상된 Level-3 복사계 토양 습도 제품(SPL3SMP_E)은 SMAP 향상된 L2 복사계 반 궤도 9km EASE-Grid 토양 습도 버전 5(SPL2SMP_E) 데이터를 일일 그리드 합성한 것입니다. SMAP 밝기 온도에서 토양 습도 도출은 Level-2 처리에서 이루어집니다. 토양 습도 알고리즘 및 보조 데이터에 대한 자세한 내용은 SPL2SMP_E 사용자 안내서를 참조하세요. 이 데이터를 향상시키기 위해 사용된 Backus-Gilbert 최적 보간 알고리즘에 대한 정보는 SPL1CTB_E 사용자 안내서를 참조하세요.
</details>

<details>
<summary>2.4 Processing</summary>

SPL3SMP_E 데이터 세트는 일일 전 세계 및 북극 제품입니다. 24시간 동안 획득된 개별 SPL2SMP_E 반 궤도 파일을 합성하여 추출된 토양 습도의 일일 다중 궤도 전 세계 또는 극지방 지도를 생성합니다. SPL2SMP_E 스와스가 겹치는 위도 약 +/- 65도 이상에서는 주어진 그리드 셀에서 여러 데이터 포인트를 합성하기 위한 세 가지 옵션이 고려되었습니다:
1. 가장 최근의(또는 마지막) 데이터 포인트 사용
2. 그리드 셀 내의 모든 데이터 포인트 평균
3. SMAP 하강 통과에서 도출된 관찰의 경우 6:00 a.m. 지역 태양 시간(LST)과 가장 가까운 데이터 포인트를, 상승 통과에서 도출된 관찰의 경우 6:00 p.m. LST와 가장 가까운 데이터 포인트를 선택

현재 SPL3SMP_E 제품에 대한 접근 방식은 세 번째 옵션을 사용하는 것입니다. 즉, 하강 통과와 상승 통과에서 각각 6:00 a.m. LST 및 6:00 p.m. LST에 가장 가까운 관찰을 선택하여 Level-3 합성을 수행합니다. 주어진 L2 반 궤도 그래뉼의 타임스탬프(yyyymmddThhmmss)는 UTC로 표현되며, hhmmss 부분만 지역 태양 시간으로 변환됩니다(O'Neill et al., 2021a).
</details>

<details>
<summary>2.5 Quality, Errors, and Limitations</summary>

### 2.5.1 Error Sources

인위적인 전파 간섭(RFI)은 주로 지상 기반 감시 레이더에서 발생하며, 이는 L-밴드 주파수에서 레이더와 복사계 측정을 오염시킬 수 있습니다. SMAP 레이더와 복사계 전자 기기 및 알고리즘에는 RFI의 영향을 완화하기 위한 설계 기능이 포함되어 있습니다. SMAP 복사계는 시간 및 주파수 다양성, 커토시스 감지, 임계값 사용을 결합하여 RFI를 감지하고, 가능한 경우 RFI를 완화하는 방법을 구현합니다(Bringer et al., 2021).

Level-2/3 복사계 데이터는 또한 통신 링크 및 메모리 저장 장치의 잡음에 의해 발생하는 비트 오류를 포함할 수 있습니다. 오류 원인에 대한 자세한 내용은 ATBD의 4.6장을 참조하십시오(O'Neill et al., 2021a).

### 2.5.2 Quality Assessment

SMAP 제품은 품질을 평가할 수 있는 여러 수단을 제공합니다. 각 제품에는 비트 플래그, 불확실성 측정, 및 품질 정보를 제공하는 파일 수준 메타데이터가 포함됩니다. 이 제품에 포함된 특정 비트 플래그, 불확실성 측정, 및 파일 수준 메타데이터에 대한 정보는 제품 사양 문서(Chan & Dunbar, 2021)를 참조하십시오. 이러한 데이터의 품질에 대한 자세한 내용은 평가 보고서(O'Neill et al., 2021b)를 참조하십시오. 각 HDF5 파일에는 NSIDC DAAC에 전달되기 전에 JPL에서 SDS에 의해 설정된 품질 평가(QA) 메타데이터 플래그가 포함된 메타데이터가 포함됩니다. 또한 각 데이터 파일과 관련된 .qa 파일 확장자를 가진 별도의 QA 파일이 있습니다. QA 파일은 연결된 데이터 파일의 품질을 보다 잘 평가할 수 있도록 통계 정보를 포함하는 ASCII 텍스트 파일입니다.

### 2.5.3 Data Flags

입력된 SMAP 데이터와 보조 데이터에서 생성된 비트 플래그는 검색 품질을 결정하는 데 사용됩니다. 보조 데이터는 일시적인 수분에 대한 보정과 같은 처리의 특정 측면을 결정하거나, 강수 플래그와 같은 검색 품질을 결정하는 데 도움이 됩니다. 이러한 플래그는 위성이 지나갈 때 지표가 얼어 있거나, 눈으로 덮여 있거나, 홍수가 나거나, 강수가 발생 중인지를 나타냅니다. 다른 플래그는 급경사 지형, 도시 지역, 조밀한 숲, 또는 영구적인 눈/얼음 지역에 대한 마스크가 적용되고 있는지를 나타냅니다.
</details>

<details>
  <summary>Retrieval Quality Flag Definition</summary>

  ### Retrieval Quality Flag Definition

  이 표는 **"토양 습도 검색 품질 플래그 정의"**를 나타냅니다. 이 표는 SMAP Enhanced L3 Radiometer 제품에서 토양 습도 데이터를 검색할 때 각 비트(Bit)에 할당된 정보를 설명하고 있습니다. 각 비트는 특정 품질 관련 정보를 나타내며, 각 비트의 값에 따라 검색이 성공했는지, 시도했는지 등의 상태를 나타냅니다.

  | Bit  | Retrieval Information    | Bit Value | Interpretation                                        |
  |------|--------------------------|-----------|-------------------------------------------------------|
  | 0    | Recommended Quality       | 0         | 토양 습도 검색이 권장 품질을 가짐                      |
  |      |                          | 1         | 토양 습도 검색이 권장 품질을 갖지 않음                |
  | 1    | Retrieval Attempted       | 0         | 토양 습도 검색이 시도됨                                |
  |      |                          | 1         | 토양 습도 검색이 건너뛰어짐                            |
  | 2    | Retrieval Successful      | 0         | 토양 습도 검색이 성공적이었음                          |
  |      |                          | 1         | 토양 습도 검색이 성공적이지 않았음                    |
  | 3    | Retrieval Successful      | 0         | 동결/해동 상태 검색이 성공적이었음                    |
  |      |                          | 1         | 동결/해동 상태 검색이 성공적이지 않았음               |
  | 4-15 | Undefined                 | 0         | 사용되지 않음                                          |

  ### 설명:
  - **Bit 0:** 권장 품질 여부를 나타냄. 
  - **Bit 1:** 토양 습도 검색이 시도되었는지 여부.
  - **Bit 2:** 검색이 성공적이었는지 여부.
  - **Bit 3:** 동결/해동 상태 검색 성공 여부.
  - **Bit 4-15:** 사용되지 않음 (미정의).

</details>
<details>
  <summary>Surface Flag Bit Definitions</summary>

  ### Surface Flag Bit Definitions
  
  Surface Flag에 대한 설명입니다. Bit 0에서 Bit 9까지의 플래그가 각기 다른 정보들을 나타냅니다.

  | Bit | Flag Name               | Bit Value | Interpretation                                                            |
  |-----|-------------------------|-----------|---------------------------------------------------------------------------|
  | 0   | Open Water Flag          | 0         | 물의 비율이 0.00-0.05: 토양 습도를 검색하고 권장 품질로 플래그를 설정     |
  |     |                         | 1         | 물의 비율이 0.05-0.50: 토양 습도를 검색하고 불확실한 품질로 플래그를 설정 |
  |     |                         |           | 물의 비율이 0.50-1.00: 토양 습도를 검색하지 않음, 플래그만 설정          |
  | 1   | Open Water Flag (MOD44W) | 0         | MOD44W 데이터베이스를 기반으로 설정된 물 비율                              |
  |     |                         | 1         | Bit 0과 동일한 값                                                         |
  | 3   | Urban Area Flag          | 0         | 도심 지역의 비율이 0.00-0.25: 토양 습도를 검색하고 권장 품질로 설정       |
  |     |                         | 1         | 도심 지역의 비율이 0.25-1.00: 토양 습도를 검색하고 불확실한 품질로 설정   |
  | 4   | Precipitation Flag       | 0         | 강수량이 0–1 mm/hr: 토양 습도를 검색하고 권장 품질로 플래그 설정          |
  |     |                         | 1         | 강수량이 1–25.4 mm/hr: 토양 습도를 검색하고 불확실한 품질로 플래그 설정  |
  |     |                         |           | 강수량이 25.4 mm/hr 이상: 토양 습도 검색하지 않음, 플래그만 설정          |
  | 5   | Snow Flag                | 0         | 눈의 비율이 0.00-0.05: 토양 습도를 검색하고 권장 품질로 플래그 설정       |
  |     |                         | 1         | 눈의 비율이 0.05-0.50: 불확실한 품질로 플래그를 설정하고 토양 습도 검색   |
  |     |                         |           | 눈의 비율이 0.50 이상: 토양 습도를 검색하지 않음, 플래그만 설정           |
  | 7   | Frozen Ground Flag       | 0         | 동결 상태 비율이 0.00-0.05: 토양 습도를 검색하고 권장 품질로 설정         |
  |     |                         | 1         | 동결 상태 비율이 0.05-0.50: 불확실한 품질로 설정하고 토양 습도 검색       |
  |     |                         |           | 동결 상태 비율이 0.50 이상: 토양 습도를 검색하지 않음, 플래그만 설정      |
  | 9   | Mountainous Area Flag    | 0         | 경사 표준 편차가 0.0-3.0°: 토양 습도를 검색하고 권장 품질로 설정          |
  |     |                         | 1         | 경사 표준 편차가 3.0°-6.0°: 불확실한 품질로 플래그를 설정하고 검색        |
  |     |                         |           | 경사 표준 편차가 6.0° 이상: 검색하지 않음, 플래그만 설정                  |

  ### 설명:
  - **Open Water Flag (Bits 0-1):** 물의 비율에 따라 검색 품질을 플래그로 설정.
  - **Urban Area Flag (Bit 3):** 도심 지역의 비율에 따라 검색 품질을 설정.
  - **Precipitation Flag (Bit 4):** 강수량에 따라 검색 여부와 품질을 결정.
  - **Snow Flag (Bit 5):** 눈의 비율에 따라 검색 품질을 플래그로 설정.
  - **Frozen Ground Flag (Bits 7-8):** 동결 상태 비율에 따라 검색 품질을 설정.
  - **Mountainous Area Flag (Bit 9):** 경사 표준 편차에 따라 검색 품질을 플래그로 설정.
</details>

<details>
  <summary>Data Fields for Soil_Moisture_Retrieval_Data_AM/PM and Soil_Moisture_Retrieval_Data_Polar_AM/PM Groups</summary>

| **Data Field Name**                 | **Type**  | **Byte** | **Unit** | **Valid Min** | **Valid Max** | **Fill/Gap Value** | **Derivation Method(s)** |
|-------------------------------------|-----------|----------|----------|---------------|---------------|--------------------|--------------------------|
| EASE_column_index                   | Uint16    | 2        | N/A      | 0             | 963           | 65534              | 2                        |
| EASE_row_index                      | Uint16    | 2        | N/A      | 0             | 405           | 65534              | 2                        |
| albedo* (albedo_dca | _scah | _scav) | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 6                        |
| boresight_incidence                  | Float32   | 4        | degrees  | 0             | 90            | -9999.0            | 1                        |
| bulk_density                         | Float32   | 4        | N/A      | 0             | 2.65          | -9999.0            | 6                        |
| clay_fraction                        | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 6                        |
| freeze_thaw_fraction                 | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 6                        |
| grid_surface_status                  | Uint16    | 2        | N/A      | 0             | 1             | 65534              | 7                        |
| landcover_class                      | Uint8     | 1        | N/A      | 0             | 16            | 254                | 6                        |
| landcover_class_fraction             | Uint8     | 1        | N/A      | 0             | 1             | -9999.0            | 6                        |
| latitude                             | Float32   | 4        | degrees  | -90           | 90            | -9999.0            | 2                        |
| latitude_centroid                    | Float32   | 4        | degrees  | -90           | 90            | -9999.0            | 1                        |
| longitude                            | Float32   | 4        | degrees  | -180          | 180           | -9999.0            | 2                        |
| longitude_centroid                   | Float32   | 4        | degrees  | -180          | 180           | -9999.0            | 1                        |
| radar_water_body_fraction            | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 6                        |
| retrieval_qual_flag*                 | Uint16    | 2        | N/A      | 0             | 65536         | 65534              | 4                        |
| roughness_coefficient*               | Float32   | 4        | N/A      | 0             | 3             | -9999.0            | 6                        |
| soil_moisture*                       | Float32   | 4        | m³/m³    | 0.02          | soil porosity | -9999.0            | 4                        |
| soil_moisture_error                  | Float32   | 4        | m³/m³    | 0.02          | soil porosity | -9999.0            | 4                        |
| static_water_body_fraction           | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 6                        |
| surface_flag                         | Uint16    | 2        | N/A      | 0             | 65536         | 65534              | 4                        |
| surface_temperature                  | Float32   | 4        | K        | 253.15        | 313.15        | -9999.0            | 6                        |
| surface_water_fraction_mb_h          | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 1                        |
| surface_water_fraction_mb_v          | Float32   | 4        | N/A      | 0             | 1             | -9999.0            | 1                        |
| tb_3_corrected                       | Float32   | 4        | K        | -50           | 50            | -9999.0            | 1                        |
| tb_4_corrected                       | Float32   | 4        | K        | -50           | 50            | -9999.0            | 1                        |
| tb_h_corrected                       | Float32   | 4        | K        | 0             | 330           | -9999.0            | 1                        |
| tb_h_uncorrected                     | Float32   | 4        | K        | 0             | 340           | -9999.0            | 1                        |
| tb_qual_flag_3                       | Uint16    | 2        | N/A      | 0             | 65536         | 65534              | 4                        |
| tb_qual_flag_4                       | Uint16    | 2        | N/A      | 0             | 65536         | 65534              | 4                        |
| tb_qual_flag_h                       | Uint16    | 2        | N/A      | 0             | 65536         | 65534              | 4                        |
| tb_qual_flag_v                       | Uint16    | 2        | N/A      | 0             | 65536         | 65534              | 4                        |
| tb_time_seconds                      | Float64   | 8        | seconds  | N/A           | N/A           | -9999.0            | 1                        |
| tb_time_utc                          | Char24    | 24       | N/A      | 2015-01-31T00:00:00.000Z | N/A           | N/A | 1                        |
| tb_v_corrected                       | Float32   | 4        | K        | 0             | 330           | -9999.0            | 1                        |
| tb_v_uncorrected                     | Float32   | 4        | K        | 0             | 340           | -9999.0            | 1                        |
| vegetation_opacity*                  | Float32   | 4        | N/A      | 0.01          | 5             | -9999.0            | 6                        |
| vegetation_opacity(_dca              | Float32   | 4        | N/A      | 0.01          | 5             | -9999.0            | 5                        |
| vegetation_opacity(_scah | _scav)    | Float32   | 4        | N/A      | 0.01          | 5             | -9999.0            | 6                        |
| vegetation_water_content             | Float32   | 4        | kg/m²    | 0.0           | 30.0          | -9999.0            | 6                        |

</details>


# 3. Soil Moisture Retrieval Data (AM)
This dataset contains various soil moisture-related measurements collected via satellite. Below are the variables available in this dataset, with explanations and sample data values.

<details>
  <summary><b>EASE_column_index</b></summary>

  * **Description**: 
    * The column index of the Equal-Area Scalable Earth Grid (EASE) for the dataset.

  * **Sample Data**: 
    * `[[0, 1, 2, ..., 3853, 3854, 3855], [0, 1, 2, ..., 3853, 3854, 3855], ... [65534, 65534, 65534, ..., 65534, 65534, 65534]]`
</details>

<details>
  <summary><b>EASE_row_index</b></summary>

  * **Description**: 
    * The row index of the Equal-Area Scalable Earth Grid (EASE) for the dataset.
    
  * **Sample Data**: 
    * `[[0, 0, 0, ..., 0, 0, 0], [1, 1, 1, ..., 1, 1, 1], ... [65534, 65534, 65534, ..., 65534, 65534, 65534]]`
</details>

<details>
  <summary><b>albedo(지표면 반사율)</b></summary>

  * **Description**: 
    * Surface reflectance of solar radiation. Missing values are marked with -9999.
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
  * **Category**:
    * albedo_dca
    * albedo_scah
    * albedo_scav
</details>
<details>
  <summary><b>boresight_incidence(센서가 바라보는 입사각)</b></summary>

  * **Description**: 
    * The boresight incidence angle is the angle at which the radar signal strikes the Earth's surface. This angle affects the radar return signal and is critical for interpreting radar data.
  
  * **Sample Data**: 
    * `[[39.97724, 39.977257, 39.97728, ..., 39.98019, 39.98021, 39.980232], [39.977066, 39.977097, 39.97712, ..., 39.98063, 39.980633, 39.980644], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>bulk_density(토양의 밀도)</b></summary>

  * **Description**: 
    * Bulk density refers to the density of the soil, which is important for analyzing water retention and soil moisture.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>clay_fraction(토양 내 점토 햠량 비율)</b></summary>

  * **Description**: 
    * The fraction of clay in the soil, which can affect water retention, soil strength, and moisture content.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>freeze_thaw_fraction(동결-해동 비율)</b></summary>

  * **Description**: 
    * The fraction of the ground that is frozen or thawing, which is important for understanding seasonal changes in soil moisture.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>grid_surface_status(표면 상태-land/water/frozen)</b></summary>

  * **Description**: 
    * The status of the surface grid, which may indicate whether the grid cell is covered by land, water, or frozen ground.
  
  * **Sample Data**: 
    * `[[1, 1, 1, ..., 1, 1, 1], [1, 1, 1, ..., 1, 1, 1], ... [65534, 65534, 65534, ..., 65534, 65534, 65534]]`
</details>

<details>
  <summary><b>latitude(위도)</b></summary>

  * **Description**: 
    * Latitude of the measurement point on the Earth's surface.
  
  * **Sample Data**: 
    * `[[84.65642, 84.65642, 84.65642, ..., 84.65642, 84.65642, 84.65642], [83.95421, 83.95421, 83.95421, ..., 83.95421, 83.95421, 83.95421], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>longitude(경도)</b></summary>

  * **Description**: 
    * Longitude of the measurement point on the Earth's surface.
  
  * **Sample Data**: 
    * `[[ -179.95332, -179.85995, -179.7666, ..., 179.7666, 179.85995, 179.95332], [-179.95332, -179.85995, -179.7666, ..., 179.7666, 179.85995, 179.95332], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>
<details>
  <summary><b>longitude_centroid(경도 중심)</b></summary>

  * **Description**: 
    * The centroid longitude of the grid cell on the Earth's surface.
  
  * **Sample Data**: 
    * `[[ -179.95332, -179.85995, -179.7666, ..., 179.7666, 179.85995, 179.95332], [-179.95332, -179.85995, -179.7666, ..., 179.7666, 179.85995, 179.95332], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>radar_water_body_fraction(수체 분율)</b></summary>

  * **Description**: 
    * The fraction of the grid cell that is covered by water bodies, detected by radar.
  
  * **Sample Data**: 
    * `[[ 1.000e+00, 1.000e+00, 1.000e+00, ..., 1.000e+00, 1.000e+00, 1.000e+00], [1.000e+00, 1.000e+00, 1.000e+00, ..., 1.000e+00, 1.000e+00, 1.000e+00], ... [-9.999e+03, -9.999e+03, -9.999e+03, ..., -9.999e+03, -9.999e+03, -9.999e+03]]`
</details>

<details>
  <summary><b>retrieval_qual_flag(품질 플래그)</b></summary>

  * **Description**: 
    * A flag indicating the quality of the retrieval process.
  
  * **Sample Data**: 
    * `[[15, 15, 15, ..., 15, 15, 15], [15, 15, 15, ..., 15, 15, 15], ... [7, 7, 7, ..., 7, 7, 7]]`
</details>

<details>
  <summary><b>retrieval_qual_flag_dca(품질 플래그 - DCA)</b></summary>

  * **Description**: 
    * A specific flag indicating the quality of the DCA retrieval process.
  
  * **Sample Data**: 
    * `[[15, 15, 15, ..., 15, 15, 15], [15, 15, 15, ..., 15, 15, 15], ... [7, 7, 7, ..., 7, 7, 7]]`
</details>

<details>
  <summary><b>retrieval_qual_flag_scah(품질 플래그 - SCAH)</b></summary>

  * **Description**: 
    * A specific flag indicating the quality of the SCAH retrieval process.
  
  * **Sample Data**: 
    * `[[15, 15, 15, ..., 15, 15, 15], [15, 15, 15, ..., 15, 15, 15], ... [7, 7, 7, ..., 7, 7, 7]]`
</details>

<details>
  <summary><b>retrieval_qual_flag_scav(품질 플래그 - SCAV)</b></summary>

  * **Description**: 
    * A specific flag indicating the quality of the SCAV retrieval process.
  
  * **Sample Data**: 
    * `[[15, 15, 15, ..., 15, 15, 15], [15, 15, 15, ..., 15, 15, 15], ... [7, 7, 7, ..., 7, 7, 7]]`
</details>

<details>
  <summary><b>roughness_coefficient(거칠기 계수)</b></summary>

  * **Description**: 
    * A coefficient representing the roughness of the Earth's surface in the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>roughness_coefficient_dca(거칠기 계수 - DCA)</b></summary>

  * **Description**: 
    * The DCA-specific roughness coefficient for the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>roughness_coefficient_scah(거칠기 계수 - SCAH)</b></summary>

  * **Description**: 
    * The SCAH-specific roughness coefficient for the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>roughness_coefficient_scav(거칠기 계수 - SCAV)</b></summary>

  * **Description**: 
    * The SCAV-specific roughness coefficient for the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>
<details>
  <summary><b>soil_moisture(토양 수분)</b></summary>

  * **Description**: 
    * The soil moisture content of the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>soil_moisture_dca(토양 수분 - DCA)</b></summary>

  * **Description**: 
    * The DCA-specific soil moisture content of the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>soil_moisture_error(토양 수분 오차)</b></summary>

  * **Description**: 
    * The estimated error in the soil moisture content.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>soil_moisture_scah(토양 수분 - SCAH)</b></summary>

  * **Description**: 
    * The SCAH-specific soil moisture content of the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>soil_moisture_scav(토양 수분 - SCAV)</b></summary>

  * **Description**: 
    * The SCAV-specific soil moisture content of the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>static_water_body_fraction(정적 수체 분율)</b></summary>

  * **Description**: 
    * The fraction of the grid cell covered by static water bodies.
  
  * **Sample Data**: 
    * `[[ 1.000e+00, 1.000e+00, 1.000e+00, ..., 1.000e+00, 1.000e+00, 1.000e+00], [1.000e+00, 1.000e+00, 1.000e+00, ..., 1.000e+00, 1.000e+00, 1.000e+00], ... [-9.999e+03, -9.999e+03, -9.999e+03, ..., -9.999e+03, -9.999e+03, -9.999e+03]]`
</details>

<details>
  <summary><b>surface_flag(표면 플래그)</b></summary>

  * **Description**: 
    * A flag representing the surface characteristics of the grid cell.
  
  * **Sample Data**: 
    * `[[ 7, 7, 7, ..., 7, 7, 7], [7, 7, 7, ..., 7, 7, 7], ... [2047, 2047, 2047, ..., 2047, 2047, 2047]]`
</details>

<details>
  <summary><b>surface_temperature(표면 온도)</b></summary>

  * **Description**: 
    * The surface temperature of the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>surface_water_fraction_mb_h(수면 분율 MB H)</b></summary>

  * **Description**: 
    * The fraction of surface water measured in the horizontal polarization (MB H).
  
  * **Sample Data**: 
    * `[[ 9.9999762e-01, 9.9999762e-01, 9.9999762e-01, ..., 9.9999380e-01, 9.9999326e-01, 9.9999273e-01], [9.9996328e-01, 9.9996090e-01, 9.9995852e-01, ..., 9.9998438e-01, 9.9998438e-01, 9.9998450e-01], ... [-9.9990000e+03, -9.9990000e+03, -9.9990000e+03, ..., -9.9990000e+03, -9.9990000e+03, -9.9990000e+03]]`
</details>

<details>
  <summary><b>surface_water_fraction_mb_v(수면 분율 MB V)</b></summary>

  * **Description**: 
    * The fraction of surface water measured in the vertical polarization (MB V).
  
  * **Sample Data**: 
    * `[[ 9.9999797e-01, 9.9999803e-01, 9.9999809e-01, ..., 9.9999464e-01, 9.9999416e-01, 9.9999386e-01], [9.9996328e-01, 9.9996090e-01, 9.9995840e-01, ..., 9.9998283e-01, 9.9998283e-01, 9.9998295e-01], ... [-9.9990000e+03, -9.9990000e+03, -9.9990000e+03, ..., -9.9990000e+03, -9.9990000e+03, -9.9990000e+03]]`
</details>

<details>
  <summary><b>tb_3_corrected(TB3 보정값)</b></summary>

  * **Description**: 
    * The corrected brightness temperature for TB3 channel.
  
  * **Sample Data**: 
    * `[[ 2.9008858e+00, 2.8248014e+00, 2.7458093e+00, ..., 2.7996993e+00, 2.8306198e+00, 2.8618824e+00], [2.8651450e+00, 2.9596300e+00, 3.0571535e+00, ..., 3.5805705e+00, 3.6088581e+00, 3.6390729e+00], ... [-9.9990000e+03, -9.9990000e+03, -9.9990000e+03, ..., -9.9990000e+03, -9.9990000e+03, -9.9990000e+03]]`
</details>

<details>
  <summary><b>tb_4_corrected(TB4 보정값)</b></summary>

  * **Description**: 
    * The corrected brightness temperature for TB4 channel.
  
  * **Sample Data**: 
    * `[[ -1.3146079e+00, -1.3354278e+00, -1.3591976e+00, ..., -2.7108657e-01, -1.3545471e-01, 1.6498566e-04], [-2.7421288e+00, -2.6188624e+00, -2.4962504e+00, ..., -5.0350428e+00, -5.0467448e+00, -5.0503407e+00], ... [-9.9990000e+03, -9.9990000e+03, -9.9990000e+03, ..., -9.9990000e+03, -9.9990000e+03, -9.9990000e+03]]`
</details>

<details>
  <summary><b>tb_h_corrected(TB H 보정값)</b></summary>

  * **Description**: 
    * The corrected brightness temperature for the horizontal polarization.
  
  * **Sample Data**: 
    * `[[ 175.93846, 175.979, 176.01578, ..., 184.97371, 184.94388, 184.9044], [162.0145, 162.30997, 162.62885, ..., 172.25409, 172.33847, 172.42548], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>tb_h_uncorrected(TB H 비보정값)</b></summary>

  * **Description**: 
    * The uncorrected brightness temperature for the horizontal polarization.
  
  * **Sample Data**: 
    * `[[ 175.93846, 175.979, 176.01578, ..., 184.97371, 184.94388, 184.9044], [162.0145, 162.30997, 162.62885, ..., 172.25409, 172.33847, 172.42548], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>tb_qual_flag_3(품질 플래그 - TB3)</b></summary>

  * **Description**: 
    * A flag indicating the quality of TB3 brightness temperature.
  
  * **Sample Data**: 
    * `[[ 0, 0, 0, ..., 8192, 8192, 8192], [0, 0, 0, ..., 8192, 8192, 8192], ... [30719, 30719, 30719, ..., 30719, 30719, 30719]]`
</details>

<details>
  <summary><b>tb_qual_flag_4(품질 플래그 - TB4)</b></summary>

  * **Description**: 
    * A flag indicating the quality of TB4 brightness temperature.
  
  * **Sample Data**: 
    * `[[ 0, 0, 0, ..., 8192, 8192, 8192], [0, 0, 0, ..., 8192, 8192, 8192], ... [30719, 30719, 30719, ..., 30719, 30719, 30719]]`
</details>

<details>
  <summary><b>tb_qual_flag_h(품질 플래그 - TB H)</b></summary>

  * **Description**: 
    * A flag indicating the quality of horizontal polarization brightness temperature.
  
  * **Sample Data**: 
    * `[[ 0, 0, 0, ..., 0, 0, 0], [0, 0, 0, ..., 4, 4, 4], ... [65535, 65535, 65535, ..., 65535, 65535, 65535]]`
</details>

<details>
  <summary><b>tb_qual_flag_v(품질 플래그 - TB V)</b></summary>

  * **Description**: 
    * A flag indicating the quality of vertical polarization brightness temperature.
  
  * **Sample Data**: 
    * `[[ 0, 0, 0, ..., 0, 0, 0], [0, 0, 0, ..., 0, 0, 0], ... [65535, 65535, 65535, ..., 65535, 65535, 65535]]`
</details>

<details>
  <summary><b>tb_time_seconds(시간 - 초 단위)</b></summary>

  * **Description**: 
    * The time of observation in seconds since epoch.
  
  * **Sample Data**: 
    * `[[ 7.75816570e+08, 7.75816570e+08, 7.75816570e+08, ..., 7.75745591e+08, 7.75745591e+08, 7.75745591e+08], [7.75816578e+08, 7.75816578e+08, 7.75816578e+08, ..., 7.75745589e+08, 7.75745589e+08, 7.75745589e+08], ... [-9.99900000e+03, -9.99900000e+03, -9.99900000e+03, ..., -9.99900000e+03, -9.99900000e+03, -9.99900000e+03]]`
</details>

<details>
  <summary><b>tb_time_utc(시간 - UTC)</b></summary>

  * **Description**: 
    * The time of observation in UTC.
  
  * **Sample Data**: 
    * `[[b'2024-08-01T20:36:10.006Z', b'2024-08-01T20:36:09.917Z', b'2024-08-01T20:36:09.834Z', ..., b'2024-08-01T00:53:11.112Z', b'2024-08-01T00:53:11.049Z', b'2024-08-01T00:53:10.988Z'], [b'2024-08-01T20:36:17.504Z', b'2024-08-01T20:36:17.531Z', b'2024-08-01T20:36:17.545Z', ..., b'2024-08-01T00:53:08.521Z', b'2024-08-01T00:53:08.512Z', b'2024-08-01T00:53:08.503Z'], ... [b'N/A                     ', b'N/A                     ', b'N/A                     ', ..., b'N/A                     ', b'N/A                     ', b'N/A                     ']]`
</details>
<details>
  <summary><b>tb_v_corrected(TB V 보정값)</b></summary>

  * **Description**: 
    * The corrected brightness temperature for the vertical polarization.
  
  * **Sample Data**: 
    * `[[197.92862, 197.95929, 197.98656, ..., 203.8034, 203.79256, 203.77184], [184.7298, 184.91116, 185.12437, ..., 193.1816, 193.2263, 193.27197], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>tb_v_uncorrected(TB V 비보정값)</b></summary>

  * **Description**: 
    * The uncorrected brightness temperature for the vertical polarization.
  
  * **Sample Data**: 
    * `[[197.92862, 197.95929, 197.98656, ..., 203.8034, 203.79256, 203.77184], [184.7298, 184.91116, 185.12437, ..., 193.1816, 193.2263, 193.27197], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>vegetation_opacity(식생 불투명도)</b></summary>

  * **Description**: 
    * The opacity of vegetation cover in the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>vegetation_opacity_dca(식생 불투명도 - DCA)</b></summary>

  * **Description**: 
    * The DCA-specific opacity of vegetation cover in the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>vegetation_opacity_scah(식생 불투명도 - SCAH)</b></summary>

  * **Description**: 
    * The SCAH-specific opacity of vegetation cover in the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>vegetation_opacity_scav(식생 불투명도 - SCAV)</b></summary>

  * **Description**: 
    * The SCAV-specific opacity of vegetation cover in the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>

<details>
  <summary><b>vegetation_water_content(식생 수분함량)</b></summary>

  * **Description**: 
    * The water content in the vegetation cover of the grid cell.
  
  * **Sample Data**: 
    * `[[ -9999, -9999, -9999, ..., -9999, -9999, -9999], [-9999, -9999, -9999, ..., -9999, -9999, -9999], ... [-9999, -9999, -9999, ..., -9999, -9999, -9999]]`
</details>


