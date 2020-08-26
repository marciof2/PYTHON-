times=('Corinthians','Palmeiras','Santos','Grêmio',
'Cruzeiro','Flamengo','Vasco da Gama','Chapecoense',	
'Atlético-MG','Botafogo'	,'Athletico-PR','Bahia',
'São Paulo','Fluminense','Sport','Vitória','Coritiba',
'Avaí','Ponte Preta','Atlético-GO')

print(f'Lista de times: {times} ')
print('-='*80)
print(f'Os 5 Primeiros colocados são: {times[:5]} ')
print('-='*80)
print(f'Os últimos 4 times são: {times[-4:]} ')
print('-='*80)
print(f'Times em ordem alfabética: {sorted(times)} ')
print('-='*80)
print(f'Chapecoense está na {times.index("Chapecoense")+1}° posição')
