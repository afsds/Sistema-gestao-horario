# Sistema Gestão de Horario

# 🛡️ Sistema de Gestão de Grade Horária Acadêmica
Este projeto é um sistema web desenvolvido para gerenciar a complexa logística de horários, professores e salas de uma faculdade de tecnologia. O foco principal é a prevenção automática de conflitos e a visualização intuitiva da grade semanal.

# 🚀 Funcionalidades
Gestão de Horários
Montagem de Grade: Criação de horários semanais associando Professor, Disciplina, Turma e Sala 

Edição Manual: Flexibilidade para ajustes diretos na interface 

Visualização Multi-Filtro: Consulta de horários por turma, professor ou sala específica (RF13).

Inteligência e Regras de Negócio (Back-end)
Validação de Disponibilidade: O sistema impede que um professor seja alocado em dois horários simultâneos (RN01/RF16).

Gestão de Espaço: Bloqueio de uso duplicado de salas no mesmo período 

Persistência em CSV: Armazenamento leve e de fácil exportação para auditoria ou relatórios 

# 🛠️ Tecnologias Utilizadas
Front-end: HTML5, CSS3 (Flexbox/Grid)

Back-end: Python (Flask)

Armazenamento: Arquivos CSV (Pandas/CSV Lib)
