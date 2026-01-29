# 🏠 [WEB + ANÁLISE] Sistema de Análise e Gestão de Imóveis

Sistema desenvolvido em **Python (Flask)** para centralizar o cadastro de **imóveis** e **corretores**, permitindo a realização de **análises técnicas de viabilidade** e **comparativos estratégicos de mercado**.

A aplicação organiza dados de propriedades e profissionais em um **banco de dados relacional**, otimizando a gestão imobiliária e apoiando a tomada de decisão.

---

## 📌 Funcionalidades

### **1. Gestão de Ativos e Profissionais**

**Cadastro Estruturado**
* Cadastro detalhado de imóveis (valor, metragem, localização).
* Cadastro de corretores com CRECI e informações de contato.

**Controle Total (CRUD)**
* Listagem, edição e exclusão de imóveis.
* Listagem, edição e exclusão de corretores.
* Operações realizadas diretamente pela interface web.

**Impacto**
* Centraliza informações que antes ficavam dispersas em mensagens ou anotações, criando um histórico organizado e acessível.

---

### **2. Inteligência de Mercado e Análise**

**Análise Técnica**
* Processamento dos dados através de uma camada de serviços dedicada (`services.py`).
* Geração de métricas de viabilidade imobiliária.

**Cálculos Automáticos**
* Indicadores para precificação.
* Comparação entre imóveis.
* Redução de erros manuais.

**Impacto**
* Facilita a identificação das melhores oportunidades de investimento, eliminando processos manuais suscetíveis a falhas humanas.

---

### **3. Dashboard de Monitoramento**

**Visualização Clara**
* Dashboards e tabelas interativas.
* Consulta rápida do portfólio de imóveis e corretores.

**Interface Responsiva**
* Desenvolvido com **Bootstrap 5**.
* Compatível com desktop e dispositivos móveis.

**Impacto**
* Oferece uma visão gerencial imediata, otimizando o tempo de busca e análise de dados.

---

### **4. Persistência e Arquitetura Modular**

**Banco de Dados Relacional**
* Utiliza **SQLite** com **Flask-SQLAlchemy (ORM)**.
* Garantia de integridade e persistência dos dados.

**Arquitetura Organizada**
* Separação entre rotas, modelos e lógica de negócio (Service Layer).

**Impacto**
* Facilita manutenções futuras e permite expansão para bancos mais robustos, como PostgreSQL.

---

## 🛠️ Stack Tecnológica

* **Backend:** Python 3.11+ | Flask
* **Banco de Dados:** SQLite | Flask-SQLAlchemy
* **Frontend:** Jinja2 | Bootstrap 5
* **Arquitetura:** Service Layer

---

## 🚀 Como Executar o Projeto

### **Pré-requisitos**
* Python 3.11 ou superior instalado

### **Instalação**

```bash
pip install flask flask-sqlalchemy
