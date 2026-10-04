import streamlit as st
from paginas.login import pagina_login
from paginas.listar_usuarios import pagina_listar


st.set_page_config(page_title="Palete_Caixa",
                    page_icon="📦",
                    layout="centered")

#print(st.session_state)


if "usuario" not in st.session_state:
    st.session_state.usuario = None

#print(st.session_state) # None ninguem logado
print(st.session_state.usuario)

if st.session_state.usuario is None:
    pagina_login()

else:
    usuario = st.session_state.usuario
    is_admin = usuario.get("tipo") == "admin"

    with st.sidebar:
        tipo_bagde = ":crown: Admin" if is_admin else \
            ":bust_in_silhouette: regular"
        st.markdown(f"**Olá {usuario['razao_social']}**")
        st.caption(f"usuario `{usuario['nome_usuario']}` - {tipo_bagde}")

        st.divider()
        opcao_menu = (
            ["Modelo Palete_Caixa", "Listar Usuarios",
            "Criar Usuario", "Alterar Status", "Alterar Senha",
            "Deletar Usuario"]
            if is_admin else ("Modelo Palete_Caixa", "Alterar Senha")
        )

        pagina = st.radio("Menu", opcao_menu, index=0,
                            label_visibility="collapsed")
        st.divider()

        if st.button(":door: Sair"):
            st.session_state.usuario = None
            st.rerun()

    if pagina == "Listar Usuarios":
        pagina_listar()
             



