'''Uma empresa decidiu fazer um levantamento em relação aos candidatos que se apresentarem para preenchi- mento de vagas em seu quadro de funcionários. Supondo que você seja o programador dessa empresa, faça um programa que leia, para cada candidato, a idade, o sexo (M ou F), e a experiência no serviço (S ou N). Para encerrar a entrada de dados, digite a idade igual a zero. O programa também deve calcular e mostrar:¶
O número de candidatos do sexo feminino.
O número de candidatos do sexo masculino.
A idade média dos homens que já tem experiência no serviço.
A porcentagem dos homens com mais de 45 anos entre o total dos homens.
O número de mulheres com idade inferior a 21 anos e com experiência no serviço.
A menor idade entre as mulheres que já tem experiência no serviço.'''

menor_idade_fem = 150
quant_fem = 0
quant_exp_fem = 0
quant_masc = 0
quant_exp_masc = 0
quant_idade_masc = 0
soma_idade_masc = 0
while True:
    idade = int(input('Digite a sua idade: '))
    if idade == 0:
        break
    sexo = input("Digite o seu sexo (M ou F)\n")
    experiencia = input("Têm experiência no serviço (S ou N)\n")
    if sexo == "F":
        quant_fem = quant_fem + 1
        if experiencia == "S":
            if menor_idade_fem > idade:
                menor_idade_fem = idade
            if idade <= 21:
                quant_exp_fem = quant_exp_fem + 1
    if sexo == "M":
        quant_masc = quant_masc + 1
        if experiencia == "S":
            soma_idade_masc = soma_idade_masc + idade
            quant_exp_masc = quant_exp_masc + 1
        if (idade >= 45):
            quant_idade_masc = quant_idade_masc + 1
    if quant_fem == 0:
        menor_idade_fem = 0
print(f'O número de candidatos do sexo feminino: {quant_fem}')
print(f'O número de candidatos do sexo masculino: {quant_masc}')
print(
    f'A idade média dos homens que já tem experiência no serviço: {soma_idade_masc / quant_exp_masc}')
print(
    f'A porcentagem dos homens com mais de 45 anos entre o total dos homens: {quant_idade_masc}')
print(
    f'O número de mulheres com idade inferior a 21 anos e com experiência no serviço: {quant_exp_fem}')
print(
    f'A menor idade entre as mulheres que já tem experiência no serviço: {menor_idade_fem}')