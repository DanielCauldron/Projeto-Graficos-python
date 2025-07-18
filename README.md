
# 📈 Projeto Gráficos Interativos da COVID-19

> Compartilhando visualizações interativas dos dados da COVID-19 no Brasil usando Python, Streamlit e Plotly.

https://projeto-graficos-python-ngdjercdcwe2rkacreqgja.streamlit.app/

## ✨ Sobre o Projeto

Este projeto oferece uma aplicação web simples e intuitiva para explorar dados da COVID-19 em todos os estados brasileiros. Através de gráficos interativos, você pode analisar a evolução dos casos e óbitos de forma dinâmica, filtrando por estado e tipo de informação.

## 🚀 Funcionalidades

- 🗂️ Seleção de estado brasileiro via menu lateral
- 📊 Escolha entre “Novos Casos” ou “Novos Óbitos”
- ⏳ Visualização temporal dos dados em gráficos interativos (Plotly)
- 🌐 Interface web moderna e fácil de usar (Streamlit)
- 🔄 Dados atualizados automaticamente do repositório oficial

## 🛠️ Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/DanielCauldron/Projeto-Graficos-python.git
   cd Projeto-Graficos-python
   ```

2. **(Opcional) Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
   > Caso não exista o arquivo `requirements.txt`, instale manualmente:
   > ```bash
   > pip install streamlit pandas plotly
   > ```

4. **Execute a aplicação**
   ```bash
   streamlit run codigoBase.py
   ```

5. **Acesse o endereço fornecido pelo Streamlit no navegador.**

---

## 💻 Exemplo de Uso

Ao rodar a aplicação, use o menu lateral para escolher o estado e o tipo de informação. O gráfico será atualizado automaticamente!

## 📚 Código Principal

O código principal está no arquivo [`codigoBase.py`](codigoBase.py). Ele utiliza:
- `pandas` para manipulação dos dados;
- `plotly.express` para gráficos interativos;
- `streamlit` para interface web.

---

## 📊 Fonte dos Dados

Os dados são obtidos automaticamente do repositório:
[https://github.com/wcota/covid19br](https://github.com/wcota/covid19br)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões, melhorias e correções.

1. Faça um fork do projeto;
2. Crie uma branch para sua feature;
3. Commit suas alterações;
4. Faça um push para a branch;
5. Abra um Pull Request.

---

## ⚖️ Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙋‍♂️ Autor

Feito com dedicação por [Daniel Cauldron](https://github.com/DanielCauldron).


