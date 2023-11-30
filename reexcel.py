import re

texto = """  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 – EN SAIO   
em placas de coluna  - até 100 kN ABNT NBR 15728 / 2009 - Parte  3  
ASTM F2193 / 2020 - Anexo 2  PLACAS ÓSSEAS Ensaio de flexão 4 pontos e fadiga em flexão 4 pont os em 
placas ósseas metálicas  - até 100 kN ABNT NBR 15676 / 2017 - Partes  2 e 3 
ASTM F382 / 2017   Ensaio de flexão em placas anguladas - até 100 kN ASTM F384 / 2017 
 Ensaio de flexão em placas anguladas - até 100 kN ASTM F384 / 2017   Determinação das propriedades de placas anguladas  ABNT NBR 15709 / 2016 - Partes 
 Determinação das propriedades de placas anguladas  ABNT NBR 15709 / 2016 - Partes  1, 2 e 3 
INTERVERTEBRAL Determinação da resistência à compressão - até 100 kN ABNT NBR 15712 / 2014 - Partes  1 e 2 
ASTM F2077 / 2018 - Itens 6.3, 8  e 9 
kN ABNT NBR 15712 / 2014 - Partes  1 e 2 
ASTM F2077 / 2018 - Itens 6.4, 8  e 9 
 Determinação da resistência à torção - até 200 Nm ABNT NBR 15712 / 2014 - Partes  1 e 2 
ASTM F2077 / 2018 - Itens 6.5, 8  e 9 
 ABNT NBR 15712 / 2009 - Parte  3 
ASTM F2267 / 20 04 (Reaprovada  2018) 
100 kN ABNT NBR 15728 / 2009 - Parte  4 
ASTM F2193 / 2020 - Anexo 3  PRÓTESE PARCIAL E 
dos componentes de hastes femorais - até 35 kN ABNT NBR ISO 7206-4:2011  Emenda 1:2016 
ABNT NBR ISO 7206 / 2016 -  Parte 6 
ISO 7206 / 2010 - Parte 4  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
kN ABNT NBR ISO 7206-4:2011  Emenda 1:2016   
componente acetabular modular - até 100 kN ASTM F1820 / 2013  ABNT NBR 15670 / 2009 - Parte 
ABNT NBR 15670 / 2009 - Parte  2 
 ABNT NBR ISO 7206-10:2019 -  item 6.3 
ASTM F2009 / 2020   Determinação da resistência à desmontagem de cabeça  
modular devido ao torque - até 200 Nm ABNT NBR ISO 7206-13:2017   Determinação da resistência à compressão de 
cabeça/cone - até 100 kN ABNT NBR ISO 7206-10:2019 -  item 6.2 
200 Nm ASTM F2582 / 2008   Rugosidade ABNT NBR ISO 7206-2:2012 
 Rugosidade ABNT NBR ISO 7206-2:2012  Emenda 1:2017 
 Ensaios Dimensionais ABNT NBR ISO 7206-2:2012  Emenda 1:2017 
até 200 Nm ABNT NBR 15668 / 2009 - Parte  3 
ASTM F1264 / 2016e1 - Anexo 2   
intramedular - até 100 kN ABNT NBR 15668 / 2009 - Partes  2 e 4 
ASTM F1264 / 2016e1 - Anexos  1 e 3 
travamento - até 100 kN ABNT NBR 15668 / 2009 - Parte  5 
ASTM F1264 / 2016e1 - Anexo 4  SISTEMA DE COLUNA Ensaio de flexão/tração em montagem de sistema de 
coluna vertebral - até 100 kN ASTM F1717:2021 - Item 8.1.2  ABNT NBR 15728-7:2012 
ABNT NBR 15728-7:2012  Versão Corrigida:2013 item 8.2.3  
de coluna vertebral - até 100 kN ASTM F1717:2021 - Itens 8.1.1 e  8.2 
ABNT NBR 15728-7:2012  Versão Corrigida:2013 item 8.2.2 
vertebral - até 200 Nm ABNT NBR 15728-7:2012  Versão Corrigida:2013 item 8.2.4 
ASTM F1717:2021 - Itens 8.1.3  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
SISTEMA DE COLUNA Compressão com apoio anterior - a té 100 kN ABNT NBR ISO 12189 / 2009  SISTEMA DE COLUNA 
DE NÍVEL ÚNICO Método de avaliação estática e dinâmica - até 100 k N ASTM F2624:2012 (Reaprovada  2020) - exceto item 9.19 
IMPLANTE DENTÁRIO Ensaio de fadiga em implante dent ário - até 35 kN ISO 14801 / 2016 – exceto item  5.7 
 Ensaio de torção em implantes dentários - até 200 Nm ISO/TS 13498 / 2011  PARAFUSOS ÓSSEOS Determinação do torque de inserção e remoção de 
parafusos ósseos - até 200 Nm ABNT NBR 15675:2020 - Parte 3   ASTM F543 / 2017 - Anexo 2 
ASTM F543 / 2017 - Anexo 2   Determinação da força de arrancamento de parafusos 
ósseos - até 100 kN ABNT NBR 15675 / 2009 - Parte  4 
ASTM F543 / 2017 - Anexo 3   Determinação da resistência à torção de parafusos 
ósseos - até 200 Nm ABNT NBR 15675 / 2018 - Parte  2 
ASTM F543 / 2017 - Anexo 1   Aparafusamento - até 1 kN ASTM F543 / 2017 - Anexo 4 
 Aparafusamento - até 1 kN ASTM F543 / 2017 - Anexo 4  ABNT NBR 15675 / 2010 - Parte 
ABNT NBR 15675 / 2010 - Parte  6 
parafusos de coluna - até 200 Nm ABNT NBR 15728 / 2009 - Parte  2 
coluna - até 100 kN ABNT NBR 15728 / 2009 - Parte  2 
coluna - até 200 Nm ABNT NBR 15728 / 2009 - Parte  2 
- até 35 kN ABNT NBR ISO 14879 / 2002 -  Parte 1  
ASTM F1800 / 2019e1   Método de avaliação estática de movimento e resistê ncia 
– até 200 Nm e 100 kN ASTM F1223:2020  DISPOSITIVOS PARA 
VERTEBRAL Ensaios de subsistema de coluna - até 100 kN ABNT NBR 15728 / 2009 - Parte  6  
ASTM F1798:2021   Ensaios em parafuso de coluna - até 100 kN ASTM F2 193 / 2020 - Anexo 1 
 Ensaios em parafuso de coluna - até 100 kN ASTM F2 193 / 2020 - Anexo 1   Flexão em balanço em parafuso de coluna - até 100 kN ABNT NBR 15728 / 2009 - Parte 
 Flexão em balanço em parafuso de coluna - até 100 kN ABNT NBR 15728 / 2009 - Parte  5  
ASTM F2193 / 2020 - Anexo 4  SISTEMA DE COLUNA 
occípito-cervical - até 100 kN ASTM F2706 / 2018 - Itens 8.1.1  e 8.2.1 
 ASTM F2706 / 2018 - Item 8.1.2  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
Nm ASTM F2706 / 2018 - Itens 8.1.3  e 8.2.2 
BIOABSORVÍVEIS  Ensaio de flexão em placas bioabsorvíveis - até 100  kN ASTM F2502 / 2017 - Anexo 4   Determinação da Força de Arrancamento de Parafusos 
Bioabsorvíveis - até 100 kN ASTM F2502 / 2017 - Anexo 3   Determinação do torque de inserção de parafusos 
bioabsorvíveis - até 200 Nm ASTM F2502 / 2017 - Anexo 2   
bioabsorvíveis - até 200 Nm ASTM F2502 / 2017 - Anexo 1   Determinação das propriedades de placas e parafusos  
bioabsorvíveis - até 100 kN ABNT NBR 15998 / 2013 -  Partes 1, 2, 3, 4 e 5  
FIXADOR EXTERNO Determinação das propriedades de pi nos - até 100 kN ASTM F1541 / 2017 - Anexo 5  ABNT NBR 15669 Parte 1:2009, 
ABNT NBR 15669 Parte 1:2009,  Parte 2:2018, Parte 3:2009 
 Tração em pinos e fios ósseos - até 100 kN ABNT NBR ISO 5838 / 2013 -  Parte 1 
RECOBRIMENTO Cisalhamento em recobrimento poroso - até 100 kN ASTM F1044 / 2005  (Reaprovada 2017)e1 
 Tração em recobrimento poroso - até 100 kN ASTM F1147 / 2005  (Reaprovada 2017)e1 
 Avaliação dinâmica de recobrimento poroso - até 10 0 kN ASTM F1160 / 2014  (Reaprovada 2017)e1 
ABNT NBR ISO 6892 Parte  1:2013 Versão Corrigida:2015 
ISO 6892-1 / 2019  ASTM A370 / 2020 seção 6 a 14 
ASTM A370 / 2020 seção 6 a 14   Ensaio de fadiga axial em controle de força com 
amplitude constante – até 35 kN ASTM E466 / 2015     
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
HBW 5 / 62,5 ASTM E10:2018  ABNT NBR ISO 6506-1:2019 
ABNT NBR ISO 6506-1:2019   Ensaio de Dureza Rockwell C (HRC) 
Faixa de trabalho: 150 Kgf ASTM E18:2020, exceto itens  1.2, 5.8 e 9.2 
ABNT NBR NM ISO 6508-1:2008   ABNT NBR ISO 6508-1:2019 
ABNT NBR ISO 6508-1:2019   Ensaio de Dureza Rockwell B (HRB)  
Faixa de trabalho: 100 Kgf ASTM E18:2020, exceto itens  1.2, 5.8 e 9.2 
ABNT NBR NM ISO 6508-1:2008   ABNT NBR ISO 6508-1:2019 
ABNT NBR ISO 6508-1:2019   Ensaio de Dureza Vickers (HV) 
HV 10 ASTM E92:2017  ABNT NBR NM ISO 6507-1:2008  
ABNT NBR NM ISO 6507-1:2008   ABNT NBR ISO 6507-1:2019 
ABNT NBR ISO 6507-1:2019   Ensaio de Microdureza Vickers (HV) 
HV 0,3 ASTM E384:2017   Ensaio de Tamanho de Grão ABNT NBR 11568:2016 
 Ensaio de Tamanho de Grão ABNT NBR 11568:2016  ASTM E1382:1997 (Reaprovada 
ASTM E1382:1997 (Reaprovada  2015)  
ASTM E112:2013  ISO 643:2019   
ISO 643:2019     Ensaio de Determinação de Inclusão não Metálica  ISO 4967:2013 
 Ensaio de Determinação de Inclusão não Metálica  ISO 4967:2013  ASTM E45:2018a   
ASTM E45:2018a    ABNT NBR NM 88:2000 
ABNT NBR NM 88:2000   Ensaio de Determinação de Profundidade de 
Endurecimento ABNT NBR 14147:1998   Ensaio de Determinação de Profundidade da Camada 
Nitretada e Cementada ISO 2639:2002  ISO 18203:2016, exceto item 8.2 
ISO 18203:2016, exceto item 8.2  e Anexo B 
Descarbonetação ABNT NBR 11299:2011  ASTM E1077:14 (reapproved 
ASTM E1077:14 (reapproved  2021) 
METÁLICOS  Ensaio de corrosão por exposição à névoa salina  ABNT NBR 8094 / 1983  ASTM B117 / 2019 
ASTM B117 / 2019  ISO 9227 / 2017 
ISO 9227 / 2017   Ensaio de corrosão por exposição à atmosfera úmida 
saturada  ABNT NBR 8095 / 2015  ASTM D1735 / 2014 
ASTM D1735 / 2014     
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
Chumbo – Pb         0,003-0,008% ASTM A751:2021   ASTM E415:2017 
ASTM E415:2017  LIGAS METÁLICAS 
Zinco – Zn 0,066-0,510%  ASTM A751:2021   ASTM E1251:2017a 
ASTM E1251:2017a     
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
Zinco – Zn 0,240-36,800%  ASTM A751:2021  LIGAS METÁLICAS 
Tungstênio-W 0,030-0,120% ASTM A751:2021  ASTM E1086:2014 
ASTM E1086:2014  LIGAS METÁLICAS 
Tungstênio W 0,002-0,084% ASTM A751:2021  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
CICLO OTTO Resistência à sobretensão por curto período ABNT NBR 15754 / 2017 – item  4.3.3 
 Resistência à sobretensão por longo período ABNT NBR 15754 / 2017 – item  4.3.4 
 Sensibilidade à inversão de polaridade ABNT NBR 15754 / 2017 – item  4.3.5 
 Comportamento de sucção com a bomba emersa ABNT NBR 15754 / 2017 – item  4.2.5.1 
emersa ABNT NBR 15754 / 2017 – item  4.2.5.2 
 Ensaio de desgaste extremo ABNT NBR 15754 / 2017 – item  4.3.8 
AUTOMOTIVOS Ensaio elétrico ABNT NBR IEC 60809 / 1997 –  Item 2.7 e Seção 4 
IEC 60809:2021 – Itens 4.7 e 8  ABNT NBR IEC 60983 / 2002 – 
ABNT NBR IEC 60983 / 2002 –  Itens 2.4.5 e 2.5 
IEC 60983 / 2005 – Itens 2.4.5 e  2.5 
 Ensaio fotométrico ABNT NBR IEC 60809 / 1997 –  Itens 2.3, 2.4, 2.7 e 2.8 e Seção 
IEC 60809:2021 - Itens 4.3,  4.4, 4.7, 4.8 e 8 
ABNT NBR IEC 60983 / 2002 –  Itens 2.4.5 e 2.5 
IEC 60983 / 2005 – Itens 2.4.5 e  2.5 
 Ensaio de Vida Característica T IEC 60810 / 2017 – Item 4.3 e  Anexo A 
 Ensaio de Vida B3 IEC 60810 / 2017 – Item 4.4 e  Anexo A 
 Ensaio de Vida ABNT NBR IEC 60983 / 2002 –  Itens 2.4.2, 2.4.3 e 2.5 
IEC 60983 / 2005 – Itens 2.4.2,  2.4.3 e 2.5 
BUZINAS Ensaios para determinação do consumo ABNT NBR 7014/2017 - item  3.3.1 
 Ensaios de isolação elétrica ABNT NBR 7014/2017 - item  3.3.3 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
BUZINAS Ensaio de impermeabilidade ABNT NBR 7014/2017 - item  3.3.8 
 Ensaios de operação contínua ABNT NBR 7014/2017 - item  3.3.7 
PEÇAS AUTOMOTIVAS Emissão de perturbação eletromagn ética conduzida ABNT NBR 15754 / 2017 – Item  4.5.1 
ABNT NBR IEC/CISPR 25:2010  – Item 6.2 
 Emissão de perturbação eletromagnética radiada ABNT NBR 15754 / 2017 – Item  4.5.1 
ABNT NBR IEC/CISPR 25:2010  – Item 6.5 
IEC 61000-4-20:2010   
AUTOMOTORES Capacidade real no regime de 20h, Cr,20 ABNT NBR 15940/2019 – item  8.2 
 Reserva de capacidade real, RCr ABNT NBR 15940/2019 – item  8.3 
 Corrente de partida à frio, CCA ABNT NBR 15940/2019 – item  8.4 
 Consumo de água ABNT NBR 15940/2019 – item  8.5 
 Capacidade real em regime de 10 h (C10) ABNT NBR 15941/2019 – item  7.3 
 ABNT NBR 15941/2019 – item  7.4 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
CICLO OTTO Operação a Seco ABNT NBR 15754 / 2017 – item  4.3.2 
 Processo de amaciamento ABNT NBR 15754 / 2017 – item  4.2.2 
 Curva característica de fornecimento de combustíve l ABNT NBR 15754 / 2017 – item  4.2.3 
aplicação ABNT NBR 15754 / 2017 – item  4.3.1.1 
 Durabilidade acelerado em combustível agressivo ABNT NBR 15754 / 2017 – item  4.3.1.2 
 Comportamento de reação da válvula de retenção ABNT NBR 15754 / 2017 – item  4.2.6.2 
 Estanqueidade da válvula de retenção ABNT NBR 15754 / 2017 – item  4.2.6.3 
 Proteção contra vazamento ABNT NBR 15754 / 2017 – item  4.2.6.4 
 Resistência ao desgaste (durabilidade com impureza s) ABNT NBR 15754 / 2017 – item  4.3.7 
 Ensaio de variação de temperatura ABNT NBR 15754 / 2017 – item  4.3.6.2 
 Ensaio de partida após inchamento ABNT NBR 15754 / 2017 – item  4.3.9 
CICLO OTTO Resistência à vibração ABNT NBR 15754 / 2017 – item  4.4.1 
 Resistência ao impacto ABNT NBR 15754 / 2017 – item  4.4.2 
combustível ABNT NBR 15754 / 2017 – item  4.5.2 
AUTOMOTIVOS Resistência à vibração e choque  IEC 60810 / 2017 – Item 4.6 e  Anexo B 
ABNT NBR 15940/2019 – item  8.6 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
QUADRICICLOS Ensaio de resistência à vibração ABNT NBR 15941/2019 – item  7.5 
AUTOMOTIVOS Dimensional ABNT NBR IEC 60809 / 1997 –  Item 2.5 e Seção 4 
IEC 60809:2021 - Itens 4.5 e 8,  Anexo D e Anexo E 
ABNT NBR IEC 60983 / 2002 –  Item 2.5 
IEC 60983 / 2005 – Item 2.5   Dimensional da base da lâmpada ABNT NBR IEC 60061 / 1998 - 
 Dimensional da base da lâmpada ABNT NBR IEC 60061 / 1998 -  Parte1 
IEC 60061 / 2005 – Parte1  IEC 60061 / 2019 – Parte1 
IEC 60061 / 2019 – Parte1   Resistência à torção IEC 60810 / 2017 – Item 4.2 
 Resistência à torção IEC 60810 / 2017 – Item 4.2  ABNT NBR IEC 60983 / 2002 – 
ABNT NBR IEC 60983 / 2002 –  Itens 2.4.4 e 2.5 
IEC 60983 / 2005 – Itens 2.4.4 e  2.5 
 Resistência do Bulbo (Compressão) IEC 60810 / 2017 – Item 4.7 e  Anexo C 
SUSPENSÃO Ensaio de Durabilidade em Amortecedores ABNT NBR 13 308 / 2014 - Item 4    Ensaio de Resistência à Tração do Conjunto Amortec edor  ABNT NBR 13308 / 2014 – Item 
 Ensaio de Resistência à Tração do Conjunto Amortec edor  ABNT NBR 13308 / 2014 – Item  5 
 Ensaio de Resistência da Fixação do Assento de Mol a ABNT NBR 13308 / 2014 – Item  6 
 Ensaio de Resistência à Corrosão de Pintura ABNT NBR 13308 / 2014 – Item  7 
 Ensaio de Homologação de Haste de Amortecedor ABNT NBR 13308 / 2014 – Item  8 
 Ensaio de Verificação de Bloqueio Hidráulica ABNT NBR 13308 / 2014 – Item  9 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
para veículos rodoviários - até 50 kN ABNT NBR 6091 / 2015 - Item 7  Resolução Contran n.º 445 de 25 
AXIAIS Acoplamento cônico ABNT NBR 16130 / 2012 – Item  6.1.5 
terminal de direção ABNT NBR 16130 / 2012 – Item  6.1.6 
de direção ABNT NBR 16130 / 2012 – Item  6.1.7 
 Integridade do material ABNT NBR 16130 / 2012 – Itens  6.1.1 e 6.2.1 
ABNT NBR NM 334 / 2012  Portaria Inmetro Nº 145:2022, de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
AXIAIS Ensaios estáticos ABNT NBR 16130 / 2012 – Item  6.3 
 Ensaio de Dureza Brinell ABNT NBR ISO 6506-1:2019  ABNT NBR ISO 6506-4:2019 
ABNT NBR ISO 6506-4:2019  ABNT NBR 16130:2012  
ABNT NBR 16130:2012   Portaria Inmetro Nº 145:2022, de 
 Ensaio de Tamanho de Grão ABNT NBR 11568:2016  ABNT NBR 16130:2012  
ABNT NBR 16130:2012   ASTM E3:2011 (REAPROVADA 
ASTM E3:2011 (REAPROVADA  2017) 
Deslizamento do Pino Esférico ABNT NBR ISO 6507-4:2019  ABNT NBR 16130:2012  
ABNT NBR 16130:2012   Portaria Inmetro Nº 145:2022, de 
 Ensaio de Tempera por Indução da Carcaça ABNT NBR ISO 6507-4:2019   Ensaio de Profundidade de Dureza ABNT NBR ISO 6507-4:2019 
 Ensaio de Profundidade de Dureza ABNT NBR ISO 6507-4:2019  ABNT NBR 16130:2012  
ABNT NBR 16130:2012   Portaria Inmetro Nº 145:2022, de 
 Ensaio de Processo de Formação de Rosca externa  ABNT NBR 16130:2012   ASTM E3:2011 (Reaprovada 
ASTM E3:2011 (Reaprovada  2017) 
ASTM E407:2007 (Reaprovada  2015)e1 
 Ensaio de Avaliação Metalográfica  ABNT NBR 16130:2012  ASTM E3:2011 (REAPROVADA 
ASTM E3:2011 (REAPROVADA  2017) 
ASTM E407:2007 (Reaprovada  2015)e1 
ABNT NBR 11568: 2016  ABNT NBR NM 136:2000 
ABNT NBR NM 136:2000  Portaria Inmetro Nº 145:2022, de 
 Ensaio de Dureza Superficial ABNT NBR ISO 6507-4:2019  ABNT NBR 16130:2012 
ABNT NBR 16130:2012  Portaria Inmetro Nº 145:2022, de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
AXIAIS Ensaio de Descarbonetação Superficial ABNT NBR 16130:2012  ABNT NBR 11299:2011 
ABNT NBR 11299:2011  ASTM E3:2011 (Reaprovada 
ASTM E3:2011 (Reaprovada  2017) 
ASTM E407:2007 (Reaprovada   2015)e1 
 Rugosidade superficial ABNT NBR 16130:2012  ABNT NBR ISO 4288:2008 
ABNT NBR ISO 4288:2008  ABNT NBR ISO 4287:2002 
ABNT NBR ISO 4287:2002  ANSI/ASME B46.1:1985 
ISO 13565-1: 1996  ISO 13565-2:1996/Cor 1:1998 
ISO 13565-2:1996/Cor 1:1998  Portaria Inmetro Nº 145:2022, de 
 Ensaios Dimensionais ISO 1101 / 2017  BS EN ISO 286-1 / 2010 
BS EN ISO 286-1 / 2010  ISO 286-2 / 2013 
ISO 286-2 / 2013  ABNT NBR 6409 / 1997 
ABNT NBR 6409 / 1997   
ENCOSTO  Ensaios Dimensionais  NBR ISO 6525: 1999  ABNT NBR ISO 6525:2021 
ABNT NBR ISO 6525:2021  NBR ISO 6526: 1999  
NBR ISO 6526: 1999   ABNT NBR ISO 12301:2011 
ABNT NBR ISO 12301:2011  Portaria Inmetro Nº 145:2022, de 
 Ensaios de Dureza  ABNT NBR ISO 12301:2011   ABNT NBR ISO 4384-2:2011 
ABNT NBR ISO 4384-2:2011  Portaria Inmetro Nº 145:2022, de 
FLANGEADAS  Ensaios Dimensionais  ABNT NBR ISO 12301:2011  ABNT NBR ISO 3548-2:2010 
ABNT NBR ISO 3548-2:2010  ABNT NBR ISO 3548-3:2013 
ABNT NBR ISO 3548-3:2013  ABNT NBR 16127:2015 
ABNT NBR 16127:2015  Portaria Inmetro Nº 145:2022, de 
 Rugosidade Superficial  ABNT NBR ISO 12301:2011   ISO 1302: 2002 
ISO 1302: 2002  ABNT NBR ISO 4287: 2002 
ABNT NBR ISO 4287: 2002  ABNT NBR ISO 4288: 2008 
ABNT NBR ISO 4288: 2008  Portaria Inmetro Nº 145:2022, de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
BRONZINAS PLANAS  Ensaios Dimensionais  ABNT NBR ISO 12301:2011  ABNT NBR 16127: 2015 
ABNT NBR 16127: 2015  ABNT NBR ISO 3548-3:2013 
ABNT NBR ISO 3548-3:2013  ABNT NBR ISO 3548-2:2010 
ABNT NBR ISO 3548-2:2010  Portaria Inmetro Nº 145:2022, de 
 Rugosidade Superficial ABNT NBR ISO 12301:2011   ISO 1302: 2002 
ISO 1302: 2002  ABNT NBR ISO 4287: 2002 
ABNT NBR ISO 4287: 2002  ABNT NBR ISO 4288: 2008 
ABNT NBR ISO 4288: 2008  Portaria Inmetro Nº 145:2022, de 
Multicamadas ABNT NBR ISO 12301:2011   ABNT NBR ISO 4384-2:2011 
ABNT NBR ISO 4384-2:2011   
BUCHA Ensaios Dimensionais ABNT NBR ISO 12301:2011   ABNT NBR ISO 3547-7:2010 
ABNT NBR ISO 3547-7:2010  ABNT NBR ISO 3547-5:2010 
ABNT NBR ISO 3547-5:2010  ABNT NBR ISO 3547-1:2021 
ABNT NBR ISO 3547-1:2021  ABNT NBR ISO 4379:2010 
ABNT NBR ISO 4379:2010  ABNT NBR ISO 4379:2021 
ABNT NBR ISO 4379:2021  ABNT NBR ISO 6506-1:2019 
ABNT NBR ISO 6506-1:2019   
 Rugosidade Superficial  ABNT NBR ISO 12301:2011  ISO 1302:2002 
ISO 1302:2002  ABNT NBR ISO 4287:2002 
ABNT NBR ISO 4287:2002  ABNT NBR ISO 4288:2008 
ABNT NBR ISO 4288:2008  ABNT NBR ISO 3547-1:2021 
ABNT NBR ISO 3547-1:2021   
 Ensaios de Dureza ABNT NBR ISO 12301:2011   ABNT NBR ISO 6506-1:2019 
ABNT NBR ISO 6506-1:2019  ABNT NBR ISO 4384-2:2011 
ABNT NBR ISO 4384-2:2011   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ANÉIS DE PISTÃO Ensaios Dimensionais ABNT NBR ISO 6621-2:2009  ABNT NBR ISO 6621-4:2016 
ABNT NBR ISO 6621-4:2016  ABNT NBR ISO 6621-5:2014 
ABNT NBR ISO 6621-5:2014  Portaria Inmetro Nº 145:2022, de 
 Rugosidade Superficial ABNT NBR ISO 6621:2:2009  ABNT NBR ISO 6621-4:2016 
ABNT NBR ISO 6621-4:2016  ABNT NBR ISO 4287:2002 
ABNT NBR ISO 4287:2002  ABNT NBR ISO 4288:2008 
ABNT NBR ISO 4288:2008  Portaria Inmetro Nº 145:2022, de 
 Perda de Força Tangencial sob Efeitos de Temperatu ra ABNT NBR ISO 6621-2:2009  ABNT NBR ISO 6621-5:2014 
ABNT NBR ISO 6621-5:2014  Portaria Inmetro Nº 145:2022, de 
 Ensaio de Inspeção Visual ABNT NBR ISO 6621-5:2014  ABNT NBR ISO 6621-2:2009 
ABNT NBR ISO 6621-2:2009  ABNT NBR ISO 6621-4:2016 
ABNT NBR ISO 6621-4:2016  Portaria Inmetro Nº 145:2022, de 
 Profundidade da Camada Nitretada ABNT NBR ISO 6621-2:2009  ABNT NBR ISO 6621-4:2016 
ABNT NBR ISO 6621-4:2016  ABNT NBR NM ISO 6507-1:2008  
ABNT NBR NM ISO 6507-1:2008   ABNT NBR ISO 6507-1:2019 
ABNT NBR ISO 6507-1:2019  Portaria Inmetro Nº 145:2022, de 
LEVE DE ALUMÍNIO Ensaios Dimensionais ABNT NBR 15905:2017  ABNT NBR 15934:2017 
ABNT NBR 15934:2017  Portaria Inmetro Nº 145:2022, de 
 Ensaios de Inspeção Visual ABNT NBR 15905:2017  ABNT NBR 15934:2017 
ABNT NBR 15934:2017  ABNT NBR ISO 6506-1:2019 
ABNT NBR ISO 6506-1:2019  Portaria Inmetro Nº 145:2022, de 
 Ensaio de Verificação da Rastreabilidade ABNT NBR 15934:2017  ABNT NBR 15905:2017 
ABNT NBR 15905:2017   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LEVE DE ALUMÍNIO Ensaios de Dureza ABNT NBR 15934:2017  ABNT NBR ISO 6506-1:2019 
ABNT NBR ISO 6506-1:2019   
 Ligação Metalúrgica do Porta Anel   ABNT NBR 15934:2017   
ANÉIS TRAVA Ensaios Dimensionais  ABNT NBR 16100:2013  ABNT NBR 15933: 2013 
ABNT NBR 15933: 2013   
 Ensaio de Funcionalidade ABNT NBR 16100:2013  ABNT NBR 15933: 2013 
ABNT NBR 15933: 2013   
ANÉIS TRAVA Tenacidade ABNT NBR 16100:2013  Portaria Inmetro Nº 145:2022, de 
PINOS DE PISTÃO Profundidade de Camada Cimentada ou  Nitretada ABNT NBR ISO 18669-1:2014  ABNT NBR ISO 18669-2:2010 
ABNT NBR ISO 18669-2:2010  (Versão corrigida 2012) 
ISO 2639:2002  ISO 18203:2016, exceto item 8.2 
ISO 18203:2016, exceto item 8.2  e Anexo B 
 Ensaios Dimensionais ABNT NBR ISO 18669-1:2014  ABNT NBR ISO 18669-2:2010 
ABNT NBR ISO 18669-2:2010  (Versão corrigida 2012) 
ISO 1101:2017  Portaria Inmetro Nº 145:2022, de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
PINOS DE PISTÃO Ensaio de Dureza ABNT NBR ISO 6506-4:2019  ABNT NBR ISO 6506-1:2019 
ABNT NBR ISO 6506-1:2019  ABNT NBR NM ISO 6508-1:2008  
ABNT NBR NM ISO 6508-1:2008   ABNT NBR ISO 6508-1:2019 
ABNT NBR ISO 6508-1:2019  ABNT NBR ISO 18669-1:2014 
ABNT NBR ISO 18669-1:2014  ABNT NBR ISO 18669-2:2010 
ABNT NBR ISO 18669-2:2010  (Versão corrigida 2012) 
 Defeitos do Material  ABNT NBR ISO 18669-1:2014  ABNT NBR ISO 18669-2:2010 
ABNT NBR ISO 18669-2:2010  (Versão corrigida 2012) 
ISO 9934-1:2016  ISO 9934-2:2015 
ISO 9934-2:2015  ISO 16810:2012 
ISO 16810:2012  Portaria Inmetro Nº 145:2022, de 
 Ensaios de Inspeção Visual ABNT NBR ISO 18669-1:2014  ABNT NBR ISO 18669-2:2010 
ABNT NBR ISO 18669-2:2010  (Versão corrigida 2012) 
PINOS DE PISTÃO Rugosidade Superficial ABNT NBR ISO 18669-1:2014  ABNT NBR ISO 18669-2:2010 
ABNT NBR ISO 18669-2:2010  (Versão corrigida 2012) 
ABNT NBR ISO 4287:2002  ABNT NBR ISO 4288:2008 
ABNT NBR ISO 4288:2008  Portaria Inmetro Nº 145:2022, de 
BICICLETA Ensaios de impacto do peso contra o quadro ABNT NBR 14714 / 2013 – Item  2.1 
 Ensaio de queda do quadro ABNT NBR 14714 / 2013 – Item  2.2 
 Ensaio de fadiga do garfo rígido ABNT NBR 14714 / 2013 – Item  2.3 
BICICLETA Ensaio de fixação do eixo do pedal ABNT NBR 15444 / 2013 – Item  3.1 
 Ensaio de impacto sobre o eixo do pedal ABNT NBR 15444 / 2013 – Item  3.2 
 Ensaio estático de resistência do pedal ABNT NBR 15444 / 2013 – Item  3.3 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
BICICLETA Ensaio de impacto sobre o pedal ABNT NBR 15444 / 2013 – Item  3.4 
 Ensaio dinâmico de resistência do pedal ABNT NBR 15444 / 2013 – Item  3.5 
 Ensaio da pedivela monobloco com carga ABNT NBR 15444 / 2013 – Item  3.6 
carga dinâmica ABNT NBR 15444 / 2013 – Item  3.7 
estática ABNT NBR 15444 / 2013 – Item  3.8 
dinâmica ABNT NBR 15444 / 2013 – Item  3.9 
BICICLETA Verificação dimensional da cordoalha ABNT NBR 9295 / 2014 – Item  4.1 
 Ensaio de ruptura do terminal da cordoalha ABNT NBR 9295 / 2014 – Item  5.2 
AROS DE BICICLETA Ensaio de verificação dimensional  ABNT NBR 14732 / 2013 – Item  7.2 
 Ensaio de ovalização ABNT NBR 14732 / 2013 – Item  7.3 
 Ensaio de empeno ABNT NBR 14732 / 2013 – Item  7.4 
 Ensaios de condição de união ABNT NBR 14732 / 2013 – Item  7.5 
 Ensaio de compressão radial ABNT NBR 14732 / 2013 – Item  7.6 
AROS DE BICICLETA Resistência a corrosão ABNT NBR 14732 / 2013 – Item  7.7 
BICICLETA Dimensões de raios de bicicleta ABNT NBR 8023 / 201 3   Determinação da resistência à fadiga de raios de bi cicleta 
- até 35 kN ABNT NBR 8024 / 2013   Dimensões de niple de bicicleta ABNT NBR 8691 / 20 13 
 Dimensões de niple de bicicleta ABNT NBR 8691 / 20 13   Determinação da resistência à tração de raio e nipl e de 
bicicleta - até 100 kN ABNT NBR 8692 / 2013  CONJUNTO DE 
DE BICICLETA Ensaio de fixação - Guidão e suporte do guidão ABNT NBR 14713 / 2014 – Item  4.5 
 Ensaio de fadiga - Guidão e/ou suporte do guidão ABNT NBR 14713 / 2014 – Item  4.7 
guidões ABNT NBR 14713 / 2014 – Item  3 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
DE BICICLETA Ensaio de deformação lateral - Suporte do guidão ABNT NBR 14713 / 2014 – Item  4.3 
 Ensaio de deformação frontal - Suporte do guidão ABNT NBR 14713 / 2014 – Item  4.4 
 Ensaio de fixação - Suporte do guidão no garfo ABNT NBR 14713 / 2014 – Item  4.6 
 Ensaio de ruptura do parafuso expander ABNT NBR 14713 / 2014 – Item  4.2 
BICICLETA Ensaio de garfo de suspensão de bicicleta ABNT NBR 15966 / 2014  COMPONENTES DE 
PARA FREIO Ensaio de compressibilidade – até 470 kN ABNT NBR ISO 6310 / 2016  ISO 6310 / 2009 
ISO 6310 / 2009  ABNT NBR 9301 / 1986 
ABNT NBR 9301 / 1986  Portaria Inmetro Nº 145:2022, de 
 Ensaio de cisalhamento – até 470kN ISO 6312 / 2010  ABNT NBR 5537 / 2002 
ABNT NBR 5537 / 2002  Portaria Inmetro Nº 145:2022, de 
o crescimento ABNT NBR 5505 / 2019   
MOLA HELICOIDAL Ensaio de pré assentamento  - até 1 00 kN ABNT NBR 15989 / 2011   Ensaio de elasticidade  - até 100 kN ABNT NBR 15989  / 2011 
 Ensaio de elasticidade  - até 100 kN ABNT NBR 15989  / 2011   Ensaio de durabilidade  - até 35 kN ABNT NBR 15989 / 2011 
 Ensaio de durabilidade  - até 35 kN ABNT NBR 15989 / 2011   Ensaio de cedimento sob carga  - até 100 kN ABNT NB R 15989 / 2011 
 Ensaio de cedimento sob carga  - até 100 kN ABNT NB R 15989 / 2011   Ensaio de resistência à pintura ABNT NBR 15989 / 20 11 
 Ensaio de resistência à pintura ABNT NBR 15989 / 20 11  CORRENTE DE 
TRANSMISSÃO Ensaio dimensional ISO 10190 / 2008  ABNT NBR 16427 / 2016 item 
ABNT NBR 16427 / 2016 item  4.2 
ABNT NBR 16427:2022 item 4.2  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
TRANSMISSÃO Ensaio de Proteção da corrente de transmissão ABNT NBR 16427:2016 - item  4.1.5 
ABNT NBR 16427:2022 - item  4.1.5 
Ensaio de resistência a tração - até 100 kN ISO 10190 / 2008  ABNT NBR 16427 / 2016 item 
ABNT NBR 16427 / 2016 item  5.3.1 
ABNT NBR 16427:2022 Item  5.3.1 
 Ensaio de Exatidão de Comprimento ISO 10190/2008   
 Ensaio de medição de comprimento ABNT NBR 16427 / 2016 item  5.2 
ABNT NBR 16427:2022 Item 5.2   
Ensaio de fadiga – Até 35 kN ABNT NBR 16427 / 2016 item  5.3.2 
ABNT NBR 16427:2022 Item  5.3.2 
 Ensaio de durabilidade ABNT NBR 16427 / 2016 item  8.4 
ABNT NBR 16427:2022 item  8.4 
COROA Ensaio dimensional ISO 10190 / 2008  ABNT NBR 16427 / 2016 item 
ABNT NBR 16427 / 2016 item  7.2 
ABNT NBR 16427:2022 item 7.2   
Ensaio de dimensões do perfil da lateral do dente ABNT NBR 16427 / 2016 item  7.3 
ABNT NBR 16427:2022 item 7.3   Ensaio de medição do diâmetro do cubo e furos de 
fixação da coroa ABNT NBR 16427 / 2016 item  7.4 
ABNT NBR 16427:2022 item 7.4   
Ensaio de durabilidade ABNT NBR 16427 / 2016 item  8.4 
ABNT NBR 16427:2022 item 8.4  PINHÃO Ensaio dimensional ISO 10190 / 2008 
PINHÃO Ensaio dimensional ISO 10190 / 2008  ABNT NBR 16427 / 2016 item 
ABNT NBR 16427 / 2016 item  7.2 
ABNT NBR 16427:2022 item 7.2   Ensaio de dimensões do perfil da lateral do dente ABNT NBR 16427 / 2016 item 
 Ensaio de dimensões do perfil da lateral do dente ABNT NBR 16427 / 2016 item  7.3 
ABNT NBR 16427:2022 item 7.3   Ensaio de medição de forma e tolerância para furo 
central do pinhão ABNT NBR 16427 / 2016 item  7.5 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ABNT NBR 16427:2022 item 7.5  AUTOMOTIVA E 
PINHÃO Ensaio de durabilidade ABNT NBR 16427 / 2016 item  8.4 
ABNT NBR 16427:2022 item 8.4   
AUTOMOTORES Inspeção Visual Externa e Peso ABNT NBR 15940/2019 – item  8.1 
ABNT NBR 15914/2018 Item 5   
ABNT NBR 15914:2018 Item 5   
AUTOMOTORES Retenção do Eletrólito ABNT NBR 15940/2019 – item  8.7 
 Estanqueidade  ABNT NBR 15940/2019 – item  8.8 
QUADRICICLOS Inspeção Visual Externa ABNT NBR 15941/2019 – item  7.1 
ABNT NBR 15916/2018   Inspeção de Peso  
 Estanqueidade (obrigatório somente baterias ventila das) ABNT NBR 15941/2019 – item  6.3.2 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
QUADRICICLOS  Ensaio de corrosão por exposição à névoa salina  ABNT NBR 16427 / 2016 item  8.3 
ABNT NBR 16427:2022 item 8.3  ABNT NBR 8094 / 1983 
ABNT NBR 8094 / 1983  ARRUELA DE 
ALUMÍNIO Ensaio de Composição Química ABNT NBR ISO 12301:2011   ABNT NBR 15905:2017 
ABNT NBR 15905:2017  ABNT NBR 15934:2017 
ABNT NBR 15934:2017  ABNT NBR ISO 18669-1:2014 
ABNT NBR ISO 18669-1:2014  Portaria Inmetro Nº 145:2022, de 
AXIAIS Ensaio de Composição Química  ABNT NBR 16130:2012  ABNT NBR NM 87:2000 Errata 
ABNT NBR NM 87:2000 Errata  2:2004 
elétrico ABNT NBR 7014:2017 Item 3.3.9    Ensaios de corrosão para verificar acabamento exter no ABNT NBR 7014:2017 Item 
 Ensaios de corrosão para verificar acabamento exter no ABNT NBR 7014:2017 Item  3.3.10 
 ABNT NBR 6752:2020 Item –  4.1.4 e 4.2.4 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
BUZINAS Faixa de temperatura de funcionamento ABNT NBR 7014:2017 Item 3.3.4    Ensaios de ciclos térmicos ABNT NBR 7014:2017 Item 3.3.5  
 Ensaios de ciclos térmicos ABNT NBR 7014:2017 Item 3.3.5   AUTOMOTIVA E 
BUZINAS Ensaios de exposição térmica ABNT NBR 7014: 2017 Item 3.3.6   AUTOMOTIVA E 
BUZINAS Ensaios para determinação da frequência  ABNT NBR 7014/2017 - item  3.3.2  
ABNT NBR 5536/2011 - item 5.1  a 5.5 
Ensaio de Durabilidade ABNT NBR 5535/2011  ABNT NBR 5536/2011 - item 5.6 
ABNT NBR 5536/2011 - item 5.6  Ensaios de vibração  ABNT NBR 7014/2017 - item 
Ensaios de vibração  ABNT NBR 7014/2017 - item  3.3.11 
ABNT NBR 5536/2011 - item 5.1  a 5.5 
 ABNT NBR NM 60335-1:2010  ABNT NBR IEC 60695-2-
ABNT NBR IEC 60695-2- 10:2015 
ABNT NBR IEC 60695-2- 11:2016 
ABNT NBR IEC 60695-2- 12:2013 
ABNT NBR IEC 60695-2- 13:2013 
ABNT NBR IEC 60695-10- 2:2020 
ABNT NBR IEC 60695-11- 5:2006 
ABNT NBR IEC 60695-11- 5:2020 
ABNT NBR 16641:2018 – item  6.7 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LUMINÁRIAS Resistência à vibração ABNT NBR IEC 60598-1 / 2010 –  Item 4.20 
ABNT NBR IEC 62031:2013  IEC 62031:2014 
IEC 62031:2014  IEC 62031:2018 Item 6 
IEC 62031:2018 Item 6  ABNT NBR IEC/PAS 62560:2013  
ABNT NBR IEC/PAS 62560:2013   IEC 62560:2015  
IEC 62560:2015   ABNT NBR IEC 62612:2013 
ABNT NBR IEC 62612:2013  IEC 62612:2015 
IEC 62612:2015   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ABNT NBR 14538:2000  ABNT NBR 14539:2000 
ABNT NBR 14539:2000  ABNT NBR IEC 60061-1:1998 
ABNT NBR IEC 60061-1:1998  IEC 60061-1:2005 
IEC 60061-1:2005  IEC 60061-1:2019 
IEC 60061-1:2019   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ABNT NBR IEC 60598-1 / 2010 –  Item 9.3 e Item 10.2.1 
ABNT NBR 5101:2018 - Item  4.3 
ABNT NBR 5101:2018 - Item  4.3.3 
ABNT NBR IEC 60598-1 / 2010 -  Item 10.2.2  
ABNT NBR 5123 / 2016 – Item  5.2.4, Item 5.2.6, Item 5.2.7, Item 
ASTM G154 – Ciclo 3   Potência total do circuito  Portaria Inmetro n.º 20, de 15 de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
IEC 61000-3-2 / 2018 – Item 7   Tensão e corrente de saída do dispositivo de contro le 
 Corrente de fuga ABNT NBR IEC 60598-1 / 2010 –  Item 10.3 
 Proteção contra choque elétrico ABNT NBR IEC 60598-1 / 2010 –  Seção 8 
ABNT NBR IEC/CISPR 15:2019  – Item 8.3 
ABNT NBR IEC/CISPR 15:2019  – Itens 9.3.2 e 9.3.4.4 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ABNT NBR IEC/CISPR 15:2019  – Item 8.3 
ABNT NBR IEC/CISPR 15:2019  – Itens 9.3.2 e 9.3.4.4 
ABNT NBR 15129 / 2012 – Item  6 
ABNT NBR IEC 60598-1 / 2010 –  Seção 3 
ABNT NBR 15129 / 2012 - Item  11 
ABNT NBR IEC 60598-1 / 2010 -  Seção 5  
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LUMINÁRIAS Resistência ao torque dos parafusos e co nexões ABNT NBR IEC 60598-1 / 2010 -  Item 4.12  
 Resistência à força do vento ABNT NBR 15129 / 2012 – Item  7.3 
 Grau de proteção ABNT NBR IEC 60529 / 2017  ABNT NBR IEC 60598-1 / 2010 – 
ABNT NBR IEC 60598-1 / 2010 –  Seção 9 
 Proteção contra impactos mecânicos externos ABNT N BR IEC 62262 / 2015  INVÓLUCROS DE 
EQUIPAMENTOS Grau de proteção ABNT NBR IEC 60529 / 2017  ABNT NBR IEC 60598-1 / 2010 – 
ABNT NBR IEC 60598-1 / 2010 –  Seção 9 
 Proteção contra impactos mecânicos externos ABNT N BR IEC 62262 / 2015  EQUIPAMENTOS DE 
SOLAR Ensaio de pressão interna ABNT NBR 15747-2/2009 - item  5.2 
ABNT NBR 15747-1:2009   
Ensaio de penetração de chuva ABNT NBR 15747-2/2009 - item  5.7 
ABNT NBR 15747-1:2009  EQUIPAMENTOS DE 
Ensaio de carga  mecânica ABNT NBR 15747-2/2009 - item  5.9 
ABNT NBR 15747-1:2009   
Ensaio de resistência ao impacto ABNT NBR 15747-2/2009 - item  5.10 
ABNT NBR 15747-1:2009   
Inspeção Final ABNT NBR 15747-2/2009 – item  5.11 
ISO 9806:2013 – Item 18  ISO 9806:2017 – Item 17 
ISO 9806:2017 – Item 17  Portaria Inmetro Nº 420:2021, de 
ABNT NBR 15747-1:2009   
Ensaio de envelhecimento acelerado ASTM G155/2013 - item 9  Portaria Inmetro Nº 420:2021, de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
TÉRMICO Ensaio de resistência ao enferrujamento ABNT NBR NM 60335-1/2010 -  item 31 
ABNT NBR 16641:2018 – item  6.8 
Ensaio de envelhecimento acelerado ASTM G155/2013 - item 9  Portaria Inmetro Nº 420:2021, de 
ACOPLADO Ensaio de pressão interna ABNT NBR 15747-2/2009 - item  5.2 
ABNT NBR 15747-1:2009   
Ensaio de penetração de chuva ABNT NBR 15747-2/2009 - item  5.7 
ABNT NBR 15747-1:2009   
Ensaio de carga mecânica ABNT NBR 15747-2/2009 - item  5.9 
ABNT NBR 15747-1:2009   
Ensaio de resistência ao impacto ABNT NBR 15747-2/2009 - item  5.10 
ABNT NBR 15747-1:2009  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ACOPLADO Ensaio de envelhecimento acelerado ASTM G155/2013 - item 9   
 Ensaio de resistência ao enferrujamento ABNT NBR NM 60335-1/2010 -  item 31 
SOLAR Ensaio de exposição ABNT NBR 15747-2/2009 - item  5.4  
ABNT NBR 15747-1:2009  Ensaio de resistência ao congelamento  
ABNT NBR 15747-2/2009 - item  5.8  
ABNT NBR 15747-1:2009  Ensaio de resistência à alta temperatura  ABNT NBR 15747-2/2009 - item 
Ensaio de resistência à alta temperatura  ABNT NBR 15747-2/2009 - item  5.3  
ABNT NBR 15747-1:2009    
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
SOLAR Ensaio de choque térmico (interno) ABNT NBR 15747-2/2009 - item  5.6  
ABNT NBR 15747-1:2009  Ensaio de choque térmico (externo) ABNT NBR 15747-2/2009 - item 
Ensaio de choque térmico (externo) ABNT NBR 15747-2/2009 - item  5.5 
ABNT NBR 15747-1:2009  Desempenho térmico ISO 9459-2/1995 - item 7 
Desempenho térmico ISO 9459-2/1995 - item 7  ABNT NBR 15747-2/2009 - item 
ABNT NBR 15747-2/2009 - item  6  
ABNT NBR 15747-1:2009  EQUIPAMENTOS DE 
ABNT NBR 10185:2018  EQUIPAMENTOS DE 
SISTEMA ACOPLADO Ensaio de exposição ABNT NBR 15747-2/2009 - item  5.4  
ABNT NBR 15747-1:2009   Ensaio de resistência à alta temperatura ABNT NBR 15747-2/2009 – item  
 Ensaio de resistência à alta temperatura ABNT NBR 15747-2/2009 – item   5.3  
ABNT NBR 15747-1:2009   Ensaio de choque térmico (interno) ABNT NBR 15747-2/2009 - item 
 Ensaio de choque térmico (interno) ABNT NBR 15747-2/2009 - item  5.6  
ABNT NBR 15747-1:2009   Ensaio de choque térmico (externo) ABNT NBR 15747-2/2009 item 
 Ensaio de choque térmico (externo) ABNT NBR 15747-2/2009 item  5.5 
ABNT NBR 15747-1:2009   Desempenho térmico ISO 9459-2/1995 - item 7  
 Desempenho térmico ISO 9459-2/1995 - item 7   ABNT NBR 15747-2/2009 item 6  
ABNT NBR 15747-2/2009 item 6   Portaria Inmetro Nº 420:2021, 
ABNT NBR 15747-1:2009   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
TÉRMICO  Ensaio de corrente de fuga  ABNT NBR 16641:2018 - item  6.5  
ABNT NBR 14016:2015 – Item 3   
 Ensaio de potência absorvida ABNT NBR 16641:2018 - item  6.6  
ABNT NBR 14013:2015 – Item 3   
TÉRMICO   Ensaio de tensão suportável ABNT NBR NM 60335-1/2010 -  item 16 
ABNT NBR 16641:2018 - item  6.4  
ACOPLADO Ensaio de corrente de fuga ABNT NBR 16641:2018 - item  6.5 
ABNT NBR 14016:2015 – Item 3  Portaria Inmetro Nº 420:2021 
Ensaio de potência absorvida ABNT NBR 16641:2018 - item  6.6  
ABNT NBR 14013:2015 – Item 3  Portaria Inmetro Nº 420:2021 
Ensaio de tensão suportável ABNT NBR NM 60335-1/2010 –  item 16 
ABNT NBR 16641:2018 - item  6.4  
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LQ: 0,005 mg CN-/L ABNT NBR 12642   Determinação do pH pelo método potenciométrico. 
LQ: 0,01 mg N - NO2-N/L ABNT NBR 12619   Determinação de ferro total pelo método colorimétri co 
LQ: 0,2 mg Fe/L ABNT 13934   Determinação da alcalinidade total pelo método 
 ABNT NBR 13736    
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LQ: 2,00 mg /L ABNT NBR 13736    
LQ: 2,00 mg /L ABNT NBR 13736    
LQ: 2,00 mg /L ABNT NBR 13736    
ISO 2917:1999   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ISO 3960:2017   
ISO 1443:1973   
ISO 936:1998   
LQ: 1,00 g/100g ISO 1871: 2009  MAPA, Manual de métodos 
ISO 1442:1997   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LQ: 1,56 g/100 g ISO 6731:2010 [IDF 21:2010]   
LQ: 1,56 g/100 g ISO 6731:2010 [IDF 21:2010]   
LQ:0,2g/100g ISO 1211:2010 [IDF 1:2010]   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
no extrato seco e lipídios totais por gravimetria ISO 17189:2003 [IDF 194:2003]  Leite em pó  Determinação de gordura, matéria gorda, matéria gor da 
LQ:0,2g/100g ISO 1736:2008 [IDF 9:2008]  Caseínas e caseinatos Determinação de gordura, matéria gorda, matéria gor da 
LQ:0,2g/100g ISO 5543:2004 [IDF 127:2004]/  ISO 23319:2022 – IDF 250 
ISO 23319:2022 – IDF 250  Creme de leite e nata  
LQ:0,2g/100g ISO 2450:2008 [IDF 16:2008]  Bebida láctea 
LQ:0,2g/100g ISO 1211:2010 [IDF 1:2010]  Queijos 
LQ: 2,00 g/100g ISO 5534:2004 [IDF 4:2004] e  MAPA, Manual de métodos 
LQ:0,2g/100g ISO 1735:2004 [IDF 5]/ ISO  23319:2022 [IDF 250] 
LQ: 1,16 g/100g ISO 3727-1:2001 - IDF 80-1   Determinação de gordura, matéria gorda, matéria gor da 
LQ:0,2g/100g ISO 17189:2003 – IDF 194    Determinação de cloretos por volumetria. 
LQ: 0,20 g/100g ISO 1738:2004 – IDF 12   Determinação de extrato seco total desengordurado 
LQ: 0,30 g/100g ISO 3727-2:2001 – IDF 80-2  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LQ: 5,00 g/100g ISO 2920:2004 [IDF 58:2004]   
LQ:0,20 g/100g ISO 1737:2008 [IDF 13]   Determinação de umidade por gravimetria 
LQ: 1,16 g/100g ISO 6734:2010 [IDF 15]  Leite Condensado Determinação de gordura, matéria gorda, matéria gor da 
LQ:0,2 g/100g ISO 1737:2008 [IDF 13]   Determinação de umidade/perda por dessecação por 
gravimetria e extrato seco por cálculo ISO 6734:2010 [IDF15]  Ricota  
LQ:0,2 g/100g ISO 1854:2008 [IDF 59]   
LQ: 1,00 g/100 g ISO 1871: 2009  MAPA, Manual de métodos 
ISO 936: 1998   
ISO 2917:1999    
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ISO 3960:2017   
ISO 1442:1997   Determinação de carboidratos totais por 
ISO 1443:1973  OVOS E DERIVADOS Determinação de pH por método eletrométrico 
 ISO 1871:2009.   Determinação de cinzas/resíduo mineral fixo/resíduo  
 ABNT NBR 15714-5:2009  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
ABNT NBR 15714-3:2009  MEIO AMBIENTE  ENSAIOS BIOLÓGICOS   
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LQ: 1 UFC/100 mL ISO 16266:2006    
LQ: 1 UFC/100 mL ISO 7937:2004   Bactérias mesófilas aeróbias a 22 ± 2°C – Determina ção 
LQ: 1 UFC/mL. ISO 6222:1999   Bactérias mesófilas aeróbias a 36 ± 2°C – Determina ção 
LQ: 1 UFC/mL ISO 6222:1999   Coliformes Totais e Termotolerantes - Determinação 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
presença/ausência. ISO 6579-1:2017   Clostridium perfringens  – determinação quantitativa pela 
LQ: 1 UFC/mL ISO 7937:2004   Bolores e leveduras – determinação quantitativa pel a 
LQ: 1 UFC/mL ISO 21527-1:2008  ISO 21527-2: 2008. 
ISO 21527-2: 2008.   Estafilococos coagulase positiva – determinação 
LQ: 1 UFC/mL ISO 6888 – 1:2009/Amd 1:2003    
 ISO 4833-1:2015  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
técnica de presença/ausência ISO 11290-1:2017   Bacillus cereus  – Determinação quantitativa pela técnica 
LQ: 1 UFC/mL ISO 7932:2004   Enterobacteriaceae – determinação quantitativa pela 
LQ: 1 UFC/mL ISO 21528-2:2004   Staphylococcus aureus  – Determinação pela técnica de 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
LQ: 10 UFC/g ISO 6888-1:2019   Bacillus cereus  – determinação quantitativa pela técnica 
LQ: 10 UFC/g ISO 7932:2016   Bolores e leveduras – determinação quantitativa pel a 
LQ: 10 UFC/g ISO 21527-1:2008  ISO 21527-2:2008 
ISO 21527-2:2008   Clostridium perfringens  – determinação quantitativa pela 
LQ: 10 UFC/g ISO 7937:2004   Enterobacteriaceae  – determinação quantitativa pela 
LQ: 10 UFC/g ISO 21528-2:2017   Listeria monocytogenes  – determinação qualitativa pela 
 ISO 11290-1:2017  ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   
presença/ausência. ISO 6579-1:2017   Bactérias mesófilas aeróbias e anaeróbias facultati vas – 
LQ: 10 UFC/g ISO 4833-1:2015   Coliformes totais e coliformes termotolerantes – 
ESCOPO DA ACREDITAÇÃO – ABNT NBR ISO/IEC 17025 - EN SAIO   

"""
#alterar o nome dessa variável pelo amor de Deus
pode_passar = ['p', 'P', 'e', 'E', '-', ':', ' ', '/', 'partes', 'Partes', 'parte', 'Parte', '0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'N', 'T', 'I', 'S', 'O', 'M', 'R', 'C','F','D', 'P','a','r','t','e','s','n','x','o']
tags = ['ABNT', 'NBR', 'ISO', 'ASTM', 'Parte', 'Partes', 'Anexo', 'Anexos'] 
lista = []

def formaPalavra():
    pass

def separarTexto(texto):
    return [letra for letra in texto]

def juntarTexto(texto):
    return ''.join(texto)

def procuraTAG(lista, texto):
    for item in lista:
        if item in texto:
            match = re.search(item, texto)
            if match:
                indice_inicial = match.start()
                indice_final = match.end()
                # print("Indice inicial: {}".format(indice_inicial))
                # print("Indice final: {}".format(indice_final))
                hehe = separarTexto(texto)
                verificador(indice_inicial, hehe)

def verificador(indice_inicial, texto_separado):
    tag = []
    for i in range(indice_inicial, len(texto_separado)):
        if texto_separado[i] in pode_passar:
            print(f"Caracter permitido: {texto_separado[i]}")
            tag.append(texto_separado[i])
        else:
            print(f"Caracter não permitido: {texto_separado[i]}")
            palavra = (juntarTexto(tag))
            if any(x in palavra for x in tags):
                lista.append(palavra)
                tag = []
            else:
                tag = []
            # for x in tags:
            #     if x in palavra:
            #         lista.append(palavra)
            #         tag = []

procuraTAG(tags, texto)

for i in lista:
    print(i)



