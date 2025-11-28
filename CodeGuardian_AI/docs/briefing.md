# PROJETO: "SafeVote" - Sistema de Votação Online Auditável

**Cliente:** Investidor de Startups / Sindicato Nacional.

**Objetivo:**
Desenvolver uma proposta técnica completa para um sistema de votação online seguro, destinado a eleições de conselhos de classe e sindicatos.

**Requisitos Críticos do Cliente:**
1. **Sigilo e Integridade:** O voto deve ser secreto, mas o processo deve ser auditável (recibo de voto).
2. **Escala:** Deve suportar 10.000 votos simultâneos sem cair.
3. **Stack Tecnológica:** Backend em Python (Django) e Frontend em React.
4. **Segurança:** Proteção total contra fraude eleitoral, injeção de votos e vazamento de dados de eleitores.

**ORDEM DE SERVIÇO PARA A EQUIPE:**
WelsPlaiFi, coordene sua equipe de 7 especialistas para criar a **PROPOSTA TÉCNICA DE SOFTWARE**.
O fluxo de trabalho obrigatório é:

1. **Evelyn:** Defina Requisitos Funcionais (ex: urna virtual, recibo) e Não-Funcionais (ex: criptografia, latência).
2. **LUA:** Desenhe a Arquitetura (considere microsserviços ou filas para a carga de 10k votos, e como garantir a imutabilidade).
3. **Neo:** Faça a Modelagem de Ameaças (foco em "Man-in-the-middle", fraude interna e DDoS).
4. **CloseHeimmer:** Defina Padrões de Código (logs de auditoria imutáveis, sanitização rigorosa).
5. **Lionel:** Crie a Estratégia de Testes (Testes de Carga com JMeter/Locust e Testes de Penetração).
6. **Atlas:** Defina o Pipeline de CI/CD (assinatura digital de commits, build reprodutível).
7. **Kenosabe:** Gere o Relatório de Viabilidade e Métricas de Sucesso do projeto.

**ENTREGA FINAL:**
O WelsPlaiFi deve encerrar apresentando o resumo consolidado como a "Proposta de Software Final".