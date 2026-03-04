BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "dados_fechamentos_caixa" (
	"id"	INTEGER,
	"data_caixa"	DATE NOT NULL,
	"data_fechamento"	DATE NOT NULL DEFAULT '2025-07-31',
	"hora"	INTEGER NOT NULL DEFAULT 0,
	"minutos"	INTEGER NOT NULL DEFAULT 0,
	"usuario_id"	INTEGER NOT NULL,
	"resultado_final_cx"	REAL NOT NULL,
	"troco_final_cx"	REAL NOT NULL,
	"estoque_troco_cx"	REAL NOT NULL,
	"vendas_total"	REAL NOT NULL,
	"vendas_dinheiro_dia"	REAL NOT NULL,
	"vendas_pix_direto_cnpj"	REAL NOT NULL DEFAULT 0.00,
	"vendas_pix_direto_cpf"	REAL NOT NULL DEFAULT 0.00,
	"vendas_operadoras_maq_cartao"	REAL NOT NULL,
	"result_trocas_devs_dinheiro"	REAL NOT NULL DEFAULT 0.00,
	"result_trocas_devs_debito"	REAL NOT NULL DEFAULT 0.00,
	"result_trocas_devs_credito"	REAL NOT NULL DEFAULT 0.00,
	"result_trocas_devs_produtos"	REAL NOT NULL DEFAULT 0.00,
	"caixa_fechado"	INTEGER NOT NULL DEFAULT 0,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	"dia_loja_fechada"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("usuario_id") REFERENCES "usuarios"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "despesas" (
	"id"	INTEGER,
	"despesa"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "despesas_caixa" (
	"id"	INTEGER,
	"descricao_despesa"	TEXT,
	"valor_despesa"	REAL NOT NULL,
	"despesa_id"	INTEGER NOT NULL,
	"caixa_id"	INTEGER NOT NULL,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("caixa_id") REFERENCES "dados_fechamentos_caixa"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("despesa_id") REFERENCES "despesas"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "entradas_n_operadora_maq" (
	"id"	INTEGER,
	"caixa_id"	INTEGER NOT NULL,
	"usuario_id"	INTEGER NOT NULL,
	"valor"	REAL NOT NULL,
	"tipo_entrada_n_operadora_maq"	INTEGER NOT NULL,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("caixa_id") REFERENCES "dados_fechamentos_caixa"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("tipo_entrada_n_operadora_maq") REFERENCES "tipo_entrada_n_operadora_maq"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("usuario_id") REFERENCES "usuarios"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "fechamentos_parciais_caixa" (
	"id"	INTEGER,
	"caixa_id"	INTEGER NOT NULL,
	"data"	DATE NOT NULL,
	"hora"	INTEGER NOT NULL DEFAULT 0,
	"minutos"	INTEGER NOT NULL DEFAULT 0,
	"usuario_id"	INTEGER NOT NULL,
	"resultado_final_cx"	REAL NOT NULL,
	"troco_final_cx"	REAL NOT NULL,
	"estoque_troco_cx"	REAL NOT NULL,
	"vendas_total"	REAL NOT NULL,
	"vendas_dinheiro_dia"	REAL NOT NULL,
	"vendas_pix_direto_cnpj"	REAL NOT NULL DEFAULT 0.00,
	"vendas_pix_direto_cpf"	REAL NOT NULL DEFAULT 0.00,
	"vendas_operadoras_maq_cartao"	REAL NOT NULL,
	"result_trocas_devs_dinheiro"	REAL NOT NULL DEFAULT 0.00,
	"result_trocas_devs_debito"	REAL NOT NULL DEFAULT 0.00,
	"result_trocas_devs_credito"	REAL NOT NULL DEFAULT 0.00,
	"result_trocas_devs_produtos"	REAL NOT NULL DEFAULT 0.00,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("CAIXA_id") REFERENCES "dados_fechamentos_caixa"("id") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("usuario_id") REFERENCES "usuarios"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "observacoes_caixa" (
	"id"	INTEGER,
	"observacao_caixa"	TEXT NOT NULL,
	"caixa_id"	INTEGER NOT NULL,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("caixa_id") REFERENCES "dados_fechamentos_caixa"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "tipos_entradas_n_operadora_maq" (
	"id"	INTEGER,
	"tipo_entrada"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "trocas_devolucoes_dia" (
	"id"	INTEGER,
	"caixa_id"	INTEGER NOT NULL,
	"num_pedido_sistema"	INTEGER,
	"codigo_produto"	TEXT,
	"tipo_ent_ou_sai"	TEXT,
	"valor"	REAL NOT NULL,
	"entrada_ou_saida"	TEXT NOT NULL,
	"relevancia_caixa"	INTEGER NOT NULL DEFAULT 0,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("CAIXA_id") REFERENCES "dados_fechamentos_caixa"("id") ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS "usuarios" (
	"id"	INTEGER,
	"nome"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "vendas_dia" (
	"id"	INTEGER,
	"data"	DATE,
	"vendas_dia"	REAL NOT NULL,
	"read_app_parent"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "dados_fechamentos_caixa" VALUES (458,'2025-10-31','2025-11-01',0,0,96,0.0,1719.71,100.0,4432.01,2.71,0.0,0.0,4430.68,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (459,'2025-11-01','2025-11-02',0,0,96,0.0,187.35,100.0,3521.31,39.91,0.0,0.0,3481.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (460,'2025-11-02','2025-11-03',0,0,96,0.15,181.4,100.0,4000.0,18.9,0.0,0.0,3981.1,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (461,'2025-11-03','2025-11-04',0,0,96,-0.02,181.4,100.0,1366.52,0.02,199.0,0.0,1167.5,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (462,'2025-11-04','2025-11-05',0,0,96,-0.04,191.2,100.0,889.14,9.84,0.0,0.0,879.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (463,'2025-11-05','2025-11-06',0,0,96,0.0,191.2,100.0,2422.3,1269.0,0.0,0.0,1153.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (464,'2025-11-06','2025-11-07',0,0,96,0.0,90.15,100.0,1242.1,3.7,0.0,0.0,1238.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (465,'2025-11-07','2025-11-08',0,0,96,-0.01,90.15,100.0,1750.81,0.01,0.0,0.0,1750.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (466,'2025-11-08','2025-11-09',0,0,96,0.0,614.15,100.0,6097.8,524.0,0.0,0.0,5573.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (467,'2025-11-09','2025-11-10',0,0,96,0.0,679.95,100.0,1560.4,65.8,0.0,0.0,1494.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (468,'2025-11-10','2025-11-11',0,0,96,0.0,889.97,100.0,3912.62,210.02,0.0,0.0,3702.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (469,'2025-11-11','2025-11-12',0,0,96,0.0,376.3,100.0,1057.81,50.01,0.0,0.0,1007.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (470,'2025-11-12','2025-11-13',0,0,96,1.99,815.1,100.0,2422.11,436.81,0.0,0.0,1983.5,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (471,'2025-11-13','2026-01-02',18,20,4,-0.02,815.1,100.0,3160.22,0.02,0.0,0.0,3160.2,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (472,'2025-11-14','2026-01-02',18,30,4,0.0,815.1,100.0,5955.82,0.0,0.0,27.42,5928.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (473,'2025-11-15','2026-01-02',18,34,4,0.0,815.1,100.0,5432.3,0.0,0.0,245.7,5186.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (474,'2025-11-16','2026-01-02',18,39,4,0.0,815.1,100.0,6867.02,0.0,0.0,41.72,6825.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (475,'2025-11-17','2026-01-02',18,45,4,-0.01,815.1,100.0,1408.01,0.01,0.0,0.0,1408.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (476,'2025-11-18','2026-01-02',18,45,4,0.0,815.1,100.0,2150.3,0.0,0.0,0.0,2150.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (477,'2025-11-19','2026-01-02',18,58,4,0.0,815.1,100.0,1755.01,0.0,0.0,197.41,1557.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (478,'2025-11-20','2026-01-02',19,34,4,-0.01,815.1,100.0,2253.81,0.01,0.0,200.0,2053.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (479,'2025-11-21','2026-01-02',19,49,4,0.0,815.1,100.0,4430.81,0.0,0.0,184.61,4246.2,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (480,'2025-11-22','2026-01-03',12,28,4,0.0,815.1,100.0,4181.9,0.0,0.0,0.0,4181.9,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (481,'2025-11-23','2026-01-03',13,8,96,0.0,770.05,100.0,1329.5,154.95,0.0,0.0,1174.55,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (482,'2025-11-24','2026-01-03',13,9,96,0.0,770.05,100.0,476.2,0.0,0.0,0.0,476.2,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (483,'2025-11-25','2026-01-03',13,14,96,0.0,770.09,100.0,796.24,0.04,0.0,0.0,796.2,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (484,'2025-11-26','2026-01-03',13,17,96,0.0,814.61,100.0,3239.62,44.52,0.0,0.0,3195.1,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (485,'2025-11-27','2026-01-03',14,9,4,0.0,872.34,100.0,7133.33,57.73,2000.0,73.9,5001.7,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (486,'2025-11-28','2026-01-03',14,24,4,0.0,872.34,100.0,5148.6,0.0,0.0,239.9,4908.7,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (487,'2025-11-29','2026-01-03',14,26,4,0.0,872.34,100.0,3901.9,0.0,0.0,164.1,3737.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (488,'2025-11-30','2026-01-03',14,27,4,0.0,872.34,100.0,5366.6,0.0,0.0,252.9,5113.7,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (489,'2025-12-01','2026-01-03',16,10,4,0.0,872.34,100.0,5253.9,0.0,0.0,130.0,5123.9,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (490,'2025-12-02','2026-01-03',16,13,4,-0.01,872.34,100.0,4788.31,0.01,985.9,0.0,3802.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (491,'2025-12-03','2026-01-03',16,32,4,0.0,889.28,100.0,5121.44,16.94,0.0,43.9,5060.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (492,'2025-12-04','2026-01-03',17,48,4,-0.01,1189.28,100.0,6431.51,300.01,0.0,116.8,6014.7,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (493,'2025-12-05','2026-01-03',17,50,4,0.0,1189.28,100.0,6289.93,0.0,0.0,829.73,5460.2,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (494,'2025-12-06','2026-01-03',18,54,4,0.0,1414.18,100.0,7255.2,224.9,0.0,558.0,6472.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (495,'2025-12-07','2026-01-03',18,54,4,0.0,1414.18,100.0,5966.3,0.0,0.0,50.8,5915.5,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (496,'2025-12-08','2026-01-04',12,58,4,0.0,1651.69,100.0,2211.21,237.51,0.0,650.0,1323.7,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (497,'2025-12-09','2026-01-04',13,1,106,0.0,1651.69,100.0,5263.8,0.0,0.0,0.0,5263.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (498,'2025-12-10','2026-01-04',13,28,106,0.0,2089.82,100.0,3865.83,438.13,0.0,620.7,2807.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (499,'2025-12-11','2026-01-04',13,42,106,-0.07,1817.02,100.0,5578.97,0.07,0.0,37.5,5541.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (500,'2025-12-12','2026-01-04',13,43,106,0.0,1817.02,100.0,1682.5,0.0,0.0,49.5,1633.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (501,'2025-12-13','2026-01-04',13,44,106,0.0,1838.92,100.0,8163.7,21.9,0.0,0.0,8141.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (502,'2025-12-14','2026-01-04',13,45,106,-0.01,1838.92,100.0,7408.01,0.01,0.0,185.0,7223.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (503,'2025-12-15','2026-01-04',13,46,106,-0.01,1838.92,100.0,3216.21,0.01,0.0,21.3,3194.9,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (504,'2025-12-16','2026-01-04',14,13,106,0.0,1982.83,100.0,8420.91,143.91,0.0,3517.4,4759.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (505,'2025-12-17','2026-01-04',14,15,106,-0.02,1982.83,100.0,8157.72,0.02,0.0,41.9,8115.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (506,'2025-12-18','2026-01-04',14,26,4,0.0,2034.73,100.0,8236.2,51.9,0.0,44.9,8139.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (507,'2025-12-19','2026-01-04',14,27,4,0.0,2034.73,100.0,6426.03,0.0,0.0,207.63,6218.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (508,'2025-12-20','2026-01-04',15,24,4,0.0,151.15,100.0,13424.1,231.9,0.0,2491.4,10700.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (509,'2025-12-21','2026-01-04',16,15,4,0.0,548.85,100.0,8255.7,397.7,0.0,0.0,7858.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (510,'2025-12-22','2026-01-04',16,16,4,-0.02,548.85,100.0,12159.72,0.02,0.0,103.7,12056.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (511,'2025-12-23','2026-01-04',16,18,4,0.0,192.0,100.0,11775.3,0.0,0.0,123.8,11651.5,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (512,'2025-12-24','2026-01-04',16,37,4,0.0,276.5,100.0,7420.5,84.5,0.0,542.9,6793.1,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (513,'2025-12-25','2026-01-04',17,29,4,0.0,276.5,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1,0,1);
INSERT INTO "dados_fechamentos_caixa" VALUES (514,'2025-12-26','2026-01-04',18,2,4,0.0,396.5,100.0,5507.3,120.0,0.0,0.0,5387.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (515,'2025-12-27','2026-01-04',18,16,4,0.0,212.4,100.0,7011.5,15.9,0.0,0.0,6995.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (516,'2025-12-28','2026-01-04',18,34,4,0.0,252.4,100.0,2865.2,40.0,0.0,0.0,2825.2,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (517,'2025-12-29','2026-01-04',18,37,4,-0.01,256.15,100.0,2929.66,3.76,0.0,310.0,2615.9,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (518,'2025-12-30','2026-01-04',18,39,4,0.0,152.25,100.0,6507.3,87.0,0.0,0.0,6420.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (519,'2025-12-31','2026-01-04',19,43,4,0.0,541.25,100.0,3645.4,420.0,0.0,0.0,3225.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (520,'2026-01-01','2026-01-04',19,43,4,0.0,541.25,100.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1,0,1);
INSERT INTO "dados_fechamentos_caixa" VALUES (521,'2026-01-02','2026-01-05',10,48,96,0.0,178.9,100.0,5153.32,227.42,0.0,0.0,4925.9,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (522,'2026-01-03','2026-01-08',18,36,4,0.0,178.9,100.0,10646.6,0.0,243.0,0.0,10403.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (523,'2026-01-04','2026-01-09',16,29,4,0.0,248.5,100.0,2496.7,69.6,0.0,0.0,2427.1,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (524,'2026-01-05','2026-01-09',16,32,4,0.0,295.4,100.0,1947.5,46.9,0.0,0.0,1900.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (525,'2026-01-06','2026-01-09',16,34,4,0.0,324.1,100.0,4710.3,28.7,0.0,149.0,4532.6,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (526,'2026-01-07','2026-01-09',16,36,4,0.0,311.51,100.0,2947.41,81.41,0.0,0.0,2866.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (527,'2026-01-08','2026-01-09',16,42,4,0.0,177.05,100.0,3873.42,0.02,0.0,0.0,3873.4,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (528,'2026-01-09','2026-01-11',12,24,4,0.0,306.05,100.0,1181.0,129.0,38.0,0.0,1014.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (529,'2026-01-10','2026-01-11',12,45,4,0.0,267.95,100.0,2865.9,59.9,0.0,669.0,2137.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (530,'2026-01-11','2026-01-12',12,47,37,0.0,283.85,100.0,671.7,15.9,44.5,0.0,611.3,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (531,'2026-01-12','2026-01-14',13,0,4,0.0,283.85,100.0,1711.0,0.0,0.0,0.0,1711.0,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (532,'2026-01-13','2026-01-14',13,5,4,0.0,232.75,100.0,657.5,0.0,0.0,0.0,657.5,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (533,'2026-01-14','2026-01-15',13,5,37,0.0,510.65,100.0,2501.7,427.9,0.0,0.0,2073.8,0.0,0.0,0.0,0.0,1,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (534,'2026-01-15','2026-01-16',0,0,4,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (535,'2026-01-16','2026-01-16',0,0,4,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (536,'2026-01-17','2024-07-31',0,0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (537,'2026-01-18','2024-07-31',0,0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0);
INSERT INTO "dados_fechamentos_caixa" VALUES (538,'2026-01-18','2024-07-31',0,0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0);
INSERT INTO "despesas" VALUES (1,'Retirada Marcio');
INSERT INTO "despesas" VALUES (2,'Despesas com Àgua e afins');
INSERT INTO "despesas" VALUES (3,'Funcionários - Salários');
INSERT INTO "despesas" VALUES (4,'Limpeza Vitrine');
INSERT INTO "despesas" VALUES (5,'Materiais Limpeza');
INSERT INTO "despesas" VALUES (6,'Materiais Escritório');
INSERT INTO "despesas" VALUES (7,'Funcionários - Condução');
INSERT INTO "despesas" VALUES (8,'Funcionários - Vale');
INSERT INTO "despesas" VALUES (9,'Materiais para manutenção da loja');
INSERT INTO "despesas" VALUES (10,'Funcionários - pagamento de feriado');
INSERT INTO "despesas" VALUES (11,'Miniaturas - Fornecedor');
INSERT INTO "despesas_caixa" VALUES (1,'ajuste cx',1572.27,1,459,0);
INSERT INTO "despesas_caixa" VALUES (2,'ajuste cx',25.0,1,460,0);
INSERT INTO "despesas_caixa" VALUES (3,'salario funcionarios',1269.0,3,463,0);
INSERT INTO "despesas_caixa" VALUES (4,'ajuste cx',104.75,1,464,0);
INSERT INTO "despesas_caixa" VALUES (5,'ajuste cx',563.68,1,469,0);
INSERT INTO "despesas_caixa" VALUES (6,'condução Matheus',180.0,7,499,0);
INSERT INTO "despesas_caixa" VALUES (7,'ajuste cx',92.8,1,499,0);
INSERT INTO "despesas_caixa" VALUES (8,' - Retirada Marcio',200.0,1,481,0);
INSERT INTO "despesas_caixa" VALUES (9,'AJUSTE troco caixa - Retirada Marcio',2115.48,1,508,0);
INSERT INTO "despesas_caixa" VALUES (10,'ajuste cx - Retirada Marcio',356.85,1,511,0);
INSERT INTO "despesas_caixa" VALUES (11,' - Retirada Marcio',200.0,1,515,0);
INSERT INTO "despesas_caixa" VALUES (12,' - Retirada Marcio',190.9,1,518,0);
INSERT INTO "despesas_caixa" VALUES (13,' - Retirada Marcio',31.0,1,519,0);
INSERT INTO "despesas_caixa" VALUES (14,'retirada marcio e colocada de troco - Retirada Marcio',589.77,1,521,0);
INSERT INTO "despesas_caixa" VALUES (16,'troca do segredos das chaves - Materiais para manutenção da loja',94.0,9,526,0);
INSERT INTO "despesas_caixa" VALUES (17,'ajuste cx - Retirada Marcio',134.48,1,527,0);
INSERT INTO "despesas_caixa" VALUES (18,' - Retirada Marcio',98.0,1,529,0);
INSERT INTO "despesas_caixa" VALUES (20,'Puto, vou beber - Retirada Marcio',35.75,1,532,0);
INSERT INTO "despesas_caixa" VALUES (21,'ajuste cx - Retirada Marcio',15.35,1,532,0);
INSERT INTO "despesas_caixa" VALUES (22,' - Retirada Marcio',150.0,1,533,0);
INSERT INTO "despesas_caixa" VALUES (23,' - Retirada Marcio',217.6,1,534,0);
INSERT INTO "despesas_caixa" VALUES (24,'ajuste cx - Despesas com Àgua e afins',26.85,2,534,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (1,471,4,0.02,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (3,472,4,27.42,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (4,473,4,245.7,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (5,474,4,41.72,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (6,475,4,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (7,477,4,197.41,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (8,478,4,200.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (9,478,4,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (10,479,4,184.61,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (11,481,96,154.95,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (12,483,96,0.04,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (13,484,96,44.52,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (14,485,4,57.73,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (15,485,4,73.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (16,485,4,2000.0,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (17,486,4,239.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (18,487,4,164.1,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (19,488,4,252.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (20,489,4,130.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (21,490,4,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (22,490,4,985.9,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (23,522,4,243.0,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (24,491,4,16.94,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (25,491,4,43.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (26,492,4,300.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (28,492,4,116.8,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (29,493,4,829.73,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (30,494,4,558.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (31,494,4,224.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (32,495,4,50.8,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (33,496,4,650.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (34,496,4,237.51,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (35,498,106,240.03,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (36,498,106,118.4,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (37,498,106,79.7,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (38,498,106,472.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (39,498,106,106.8,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (40,498,106,41.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (41,499,106,0.07,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (42,499,106,37.5,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (43,500,106,49.5,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (44,501,106,21.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (45,502,106,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (46,502,106,185.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (47,503,106,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (48,503,106,21.3,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (49,504,106,3500.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (50,504,106,17.4,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (51,504,106,143.91,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (52,505,106,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (53,505,106,41.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (54,505,106,0.01,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (55,506,4,51.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (56,506,4,44.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (57,507,4,207.63,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (60,508,4,96.6,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (61,508,4,139.8,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (62,508,4,1520.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (63,508,4,735.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (64,508,4,31.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (66,508,4,200.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (67,509,4,248.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (68,509,4,99.8,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (69,509,4,49.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (70,510,4,0.02,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (71,510,4,103.7,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (72,511,4,123.8,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (73,512,4,55.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (74,512,4,29.5,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (75,512,4,510.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (76,512,4,32.9,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (77,514,4,120.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (78,515,4,15.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (79,516,4,40.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (80,517,4,3.76,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (81,517,4,310.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (82,518,4,87.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (85,519,4,420.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (87,521,96,227.42,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (89,523,4,69.6,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (90,524,4,46.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (91,525,4,28.7,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (92,525,4,149.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (93,526,4,81.41,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (94,527,4,0.02,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (95,528,4,129.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (96,528,4,38.0,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (97,529,4,59.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (98,529,4,669.0,3,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (99,530,4,44.5,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (100,530,37,15.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (101,533,37,260.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (102,533,37,149.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (103,533,37,18.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (104,534,4,38.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (107,534,4,49.9,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (108,535,4,44.8,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (109,535,4,47.0,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (110,536,37,31.5,2,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (111,536,37,1049.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (112,536,37,34.0,1,0);
INSERT INTO "entradas_n_operadora_maq" VALUES (113,536,37,210.0,1,0);
INSERT INTO "fechamentos_parciais_caixa" VALUES (1,526,'2026-01-07',12,15,4,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0);
INSERT INTO "fechamentos_parciais_caixa" VALUES (4,526,'2026-01-07',18,29,4,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0);
INSERT INTO "fechamentos_parciais_caixa" VALUES (5,530,'2026-01-11',12,46,4,0.0,267.95,100.0,16.8,0.0,0.0,0.0,16.8,0.0,0.0,0.0,0.0,0);
INSERT INTO "fechamentos_parciais_caixa" VALUES (6,533,'2026-01-14',13,6,4,0.0,232.75,100.0,1269.7,0.0,0.0,0.0,1269.7,0.0,0.0,0.0,0.0,0);
INSERT INTO "fechamentos_parciais_caixa" VALUES (7,534,'2026-01-15',20,7,4,0.0,331.05,100.0,3502.5,38.0,0.0,0.0,3464.5,0.0,0.0,0.0,0.0,0);
INSERT INTO "observacoes_caixa" VALUES (1,'apenas teste, observação... Veio o rapaz do Shop e quer falar com vc',521,0);
INSERT INTO "tipos_entradas_n_operadora_maq" VALUES (1,'dinheiro');
INSERT INTO "tipos_entradas_n_operadora_maq" VALUES (2,'PIX direto CNPJ');
INSERT INTO "tipos_entradas_n_operadora_maq" VALUES (3,'PIX diretor CPF');
INSERT INTO "trocas_devolucoes_dia" VALUES (8,511,NULL,'','0',0.0,'S',0,0);
INSERT INTO "trocas_devolucoes_dia" VALUES (9,511,NULL,'','0',0.0,'E',0,0);
INSERT INTO "trocas_devolucoes_dia" VALUES (10,511,NULL,'','0',0.0,'S',0,0);
INSERT INTO "usuarios" VALUES (4,'Marcio Suconic');
INSERT INTO "usuarios" VALUES (26,'Veronica Suconic');
INSERT INTO "usuarios" VALUES (37,'Gustavo');
INSERT INTO "usuarios" VALUES (45,'Beatriz Suconic');
INSERT INTO "usuarios" VALUES (96,'Yara');
INSERT INTO "usuarios" VALUES (106,'Matheus');
COMMIT;
