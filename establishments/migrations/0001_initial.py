# Generated by Django 4.0.6 on 2024-08-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cnes', models.BigIntegerField(verbose_name='Código CNES')),
                ('numero_cnpj_entidade', models.CharField(max_length=14, verbose_name='Número CNPJ da Entidade')),
                ('nome_razao_social', models.CharField(max_length=255, verbose_name='Nome/Razão Social')),
                ('nome_fantasia', models.CharField(max_length=255, verbose_name='Nome Fantasia')),
                ('natureza_organizacao_entidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Natureza da Organização da Entidade')),
                ('tipo_gestao', models.CharField(max_length=1, verbose_name='Tipo de Gestão')),
                ('descricao_nivel_hierarquia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição do Nível Hierárquico')),
                ('descricao_esfera_administrativa', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição da Esfera Administrativa')),
                ('codigo_tipo_unidade', models.IntegerField(verbose_name='Código Tipo de Unidade')),
                ('codigo_cep_estabelecimento', models.CharField(max_length=8, verbose_name='Código CEP do Estabelecimento')),
                ('endereco_estabelecimento', models.CharField(max_length=255, verbose_name='Endereço do Estabelecimento')),
                ('numero_estabelecimento', models.CharField(max_length=10, verbose_name='Número do Estabelecimento')),
                ('bairro_estabelecimento', models.CharField(max_length=255, verbose_name='Bairro do Estabelecimento')),
                ('numero_telefone_estabelecimento', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de Telefone do Estabelecimento')),
                ('latitude_estabelecimento_decimo_grau', models.FloatField(blank=True, null=True, verbose_name='Latitude do Estabelecimento (Decimos de Grau)')),
                ('longitude_estabelecimento_decimo_grau', models.FloatField(blank=True, null=True, verbose_name='Longitude do Estabelecimento (Decimos de Grau)')),
                ('endereco_email_estabelecimento', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Endereço de E-mail do Estabelecimento')),
                ('numero_cnpj', models.CharField(blank=True, max_length=14, null=True, verbose_name='Número CNPJ')),
                ('codigo_identificador_turno_atendimento', models.CharField(max_length=2, verbose_name='Código Identificador do Turno de Atendimento')),
                ('descricao_turno_atendimento', models.CharField(max_length=255, verbose_name='Descrição do Turno de Atendimento')),
                ('estabelecimento_faz_atendimento_ambulatorial_sus', models.CharField(max_length=3, verbose_name='Estabelecimento Faz Atendimento Ambulatorial SUS')),
                ('codigo_estabelecimento_saude', models.CharField(max_length=14, verbose_name='Código do Estabelecimento de Saúde')),
                ('codigo_uf', models.IntegerField(verbose_name='Código UF')),
                ('codigo_municipio', models.IntegerField(verbose_name='Código Município')),
                ('descricao_natureza_juridica_estabelecimento', models.CharField(max_length=4, verbose_name='Descrição da Natureza Jurídica do Estabelecimento')),
                ('codigo_motivo_desabilitacao_estabelecimento', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código Motivo Desabilitação do Estabelecimento')),
                ('estabelecimento_possui_centro_cirurgico', models.BooleanField(blank=True, default=False, null=True, verbose_name='Estabelecimento Possui Centro Cirúrgico')),
                ('estabelecimento_possui_centro_obstetrico', models.BooleanField(blank=True, default=False, null=True, verbose_name='Estabelecimento Possui Centro Obstétrico')),
                ('estabelecimento_possui_centro_neonatal', models.BooleanField(blank=True, default=False, null=True, verbose_name='Estabelecimento Possui Centro Neonatal')),
                ('estabelecimento_possui_atendimento_hospitalar', models.BooleanField(blank=True, default=False, null=True, verbose_name='Estabelecimento Possui Atendimento Hospitalar')),
                ('estabelecimento_possui_servico_apoio', models.BooleanField(blank=True, default=True, null=True, verbose_name='Estabelecimento Possui Serviço de Apoio')),
                ('estabelecimento_possui_atendimento_ambulatorial', models.BooleanField(blank=True, default=False, null=True, verbose_name='Estabelecimento Possui Atendimento Ambulatorial')),
                ('codigo_atividade_ensino_unidade', models.CharField(max_length=2, verbose_name='Código Atividade Ensino Unidade')),
                ('codigo_natureza_organizacao_unidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código Natureza Organização Unidade')),
                ('codigo_nivel_hierarquia_unidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código Nível Hierárquico Unidade')),
                ('codigo_esfera_administrativa_unidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Código Esfera Administrativa Unidade')),
            ],
            options={
                'verbose_name': 'estabelecimento',
                'verbose_name_plural': 'Estabelecimentos',
            },
        ),
    ]
