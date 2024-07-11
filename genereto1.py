# Informações detalhadas sobre executores de script do Roblox

executores = [
    {
        "nome": "Flux",
        "descrição": "Um dos executores de script mais populares para Roblox, conhecido por sua interface amigável e suporte a injeção de script.",
        "site": "https://wearedevs.net/d/Flux",
        "funções": ["Injeção de script", "Exploração de memória", "Suporte a Lua"],
        "comportamento_lua": "Flux é capaz de executar scripts Lua diretamente no ambiente do jogo. Ele suporta injeção de script para modificar o comportamento do jogo em tempo real, além de permitir a exploração da memória para encontrar variáveis e funções.",
        "exemplo_script": """
-- Exemplo de script para Flux
game:GetService("Workspace").Part.Color = Color3.new(1, 0, 0)
wait(1)
game:GetService("Workspace").Part.Color = Color3.new(0, 1, 0)
"""
    },
    {
        "nome": "Arceus X",
        "descrição": "Executor de script avançado para Roblox, oferecendo uma ampla gama de funcionalidades e atualizações frequentes.",
        "site": "https://spdmteam.com/index",
        "funções": ["Interface amigável", "Atualizações frequentes", "Compatibilidade avançada"],
        "comportamento_lua": "Arceus X possui uma interface amigável que permite aos usuários executar scripts Lua de forma avançada. Ele é conhecido por sua capacidade de suportar scripts complexos e é frequentemente atualizado para manter a compatibilidade com as últimas versões do Roblox.",
        "exemplo_script": """
-- Exemplo de script para Arceus X
game.Workspace.Part.Color = Color3.fromRGB(255, 0, 0)
wait(1)
game.Workspace.Part.Color = Color3.fromRGB(0, 255, 0)
"""
    },
    {
        "nome": "Script-Ware",
        "descrição": "Um poderoso executor de script para Roblox, com suporte a diversos scripts Lua e interface intuitiva.",
        "site": "https://wearedevs.net/d/Script-Ware",
        "funções": ["Suporte a Lua", "Exploração de memória", "Injeção de script"],
        "comportamento_lua": "Script-Ware oferece suporte robusto para scripts Lua no Roblox, permitindo aos usuários explorar a memória do jogo e injetar scripts para alterar o comportamento do jogo conforme desejado.",
        "exemplo_script": """
-- Exemplo de script para Script-Ware
game.Workspace.Part.BrickColor = BrickColor.new("Bright red")
wait(1)
game.Workspace.Part.BrickColor = BrickColor.new("Bright blue")
"""
    },
    {
        "nome": "KRNL",
        "descrição": "Executor de script gratuito e de código aberto para Roblox, com capacidades de injeção de script e suporte a Lua.",
        "site": "https://wearedevs.net/d/KRNL",
        "funções": ["Injeção de script", "Suporte a Lua", "Compatibilidade avançada"],
        "comportamento_lua": "KRNL é conhecido por ser um executor de script de código aberto para Roblox, permitindo a injeção de scripts Lua e oferecendo suporte a uma ampla gama de funcionalidades avançadas.",
        "exemplo_script": """
-- Exemplo de script para KRNL
game.Workspace.Part.Transparency = 0.5
wait(1)
game.Workspace.Part.Transparency = 0
"""
    }
]

# Imprime informações detalhadas de cada executor
for executor in executores:
    print(f"Nome: {executor['nome']}")
    print(f"Descrição: {executor['descrição']}")
    print(f"Site: {executor['site']}")
    print("Funções:")
    for func in executor['funções']:
        print(f" - {func}")
    print("Comportamento em Lua:")
    print(executor['comportamento_lua'])
    print("Exemplo de script Lua:")
    print(executor['exemplo_script'])
    print("--------------------")
