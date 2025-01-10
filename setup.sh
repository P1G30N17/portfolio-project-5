mkdir -p ~/.streamlit/
echo "\
[client]\n\
showSidebarNavigation = false\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
