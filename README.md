# Minha Comunicação CAA — V2 corrigida

Projeto Android em Python + Kivy para Comunicação Aumentativa e Alternativa.

## Recursos
- Interface para celular/tablet
- Categorias de comunicação
- Símbolos e emojis
- Frases rápidas
- Montagem de frases
- Botão de voz pelo Text-to-Speech do Android
- Preparado para personalização e expansão

## Gerar APK pelo GitHub
1. Crie um repositório no GitHub.
2. Envie todo o conteúdo deste projeto, incluindo `.github/workflows/android.yml`.
3. Abra **Actions**.
4. Selecione **Gerar APK Android**.
5. Clique em **Run workflow**.
6. Aguarde a compilação.
7. No workflow concluído, baixe o artefato **Minha-Comunicacao-CAA-APK**.

## Gerar localmente
```bash
python3 -m pip install --upgrade pip
python3 -m pip install buildozer cython==0.29.37
buildozer -v android debug
```

O APK será criado em `bin/`.
