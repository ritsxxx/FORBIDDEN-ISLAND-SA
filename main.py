from map import create_map, create_players, create_treasures
from map import show_map, SIZE, SUNK

from player import move_engineer, move_pilot

from flood import flood_island, repair_tile

from treasure import collect_treasure


# ゲームの初期設定
island = create_map()
players = create_players()
treasures = create_treasures()

# 脱出口の位置
exit_position = [1, 2]

# 財宝の数
collected = 0

# 現在のプレイヤー
turn = 0


# 勝敗を確認する関数
def check_game():

    # 脱出口が沈んだら敗北
    exit_row = exit_position[0]
    exit_col = exit_position[1]

    if island[exit_row][exit_col] == SUNK:
        return "lose"

    # プレイヤーが沈んだマスにいたら敗北
    for player in players:

        row = player["position"][0]
        col = player["position"][1]

        if island[row][col] == SUNK:
            return "lose"

    # 残っている財宝のマスが沈んだら敗北
    for treasure in treasures:

        row = treasure[0]
        col = treasure[1]

        if island[row][col] == SUNK:
            return "lose"

    # 財宝をすべて集め、2人とも脱出口に到着したら勝利
    if len(treasures) == 0:

        if players[0]["position"] == exit_position:
            if players[1]["position"] == exit_position:
                return "win"

    return "continue"


# 座標を入力する関数
def input_position():

    try:
        row = int(input("行（1～4）：")) - 1
        col = int(input("列（1～4）：")) - 1

        return row, col

    except ValueError:
        print("数字を入力してください")
        return None, None


# ゲーム開始
print("===== FORBIDDEN ISLAND =====")
print("財宝を4個集めて、2人で脱出しよう！")


# ゲームの繰り返し
while True:

    # プレイヤーを交代
    player = players[turn]

    # 1ターンの行動回数
    actions = 0

    # エンジニアの修復回数
    repairs = 0

    print("\n", player["name"], "のターンです")

    # 3アクション行う
    while actions < 3:

        show_map(island, players, treasures, exit_position)

        print("\n残りアクション：", 3 - actions)
        print("回収した財宝：", 4 - len(treasures), "/ 4")

        print("\n1：移動")
        print("2：修復")
        print("3：財宝回収")

        command = input("行動を選んでください：")

        success = False

        # 移動
        if command == "1":

            if player["role"] == "engineer":

                direction = input("移動方向（w:上 s:下 a:左 d:右）：")

                success = move_engineer(player, direction, island)

            else:

                print("移動先を入力してください")
                row, col = input_position()

                if row is not None and col is not None:
                    success = move_pilot(player, row, col, island)

        # 修復
        elif command == "2":

            if player["role"] == "engineer":

                if repairs < 2:

                    print("修復するマスを入力してください")
                    row, col = input_position()

                    if row is not None and col is not None:

                        if 0 <= row < SIZE and 0 <= col < SIZE:
                            success = repair_tile(
                                player, row, col, island
                            )

                            if success:
                                repairs = repairs + 1
                        else:
                            print("マップの範囲外です")

                else:
                    print("このターンの修復回数は上限です")

            else:
                print("パイロットは修復できません")

        # 財宝回収
        elif command == "3":

            success = collect_treasure(player, treasures)

        else:
            print("正しい番号を入力してください")

        # 成功した行動だけ回数を消費
        if success:
            actions = actions + 1

        # 勝敗を確認
        result = check_game()

        if result == "win":
            show_map(island, players, treasures, exit_position)
            print("おめでとう！ゲームクリア！")
            break

        elif result == "lose":
            show_map(island, players, treasures, exit_position)
            print("ゲームオーバー！")
            break

    # ゲームが終了していたらループを抜ける
    if result == "win" or result == "lose":
        break

    # ターン終了時に島を水没させる
    print("\n島の水没処理を行います")

    flood_island(island)

    # 水没後に勝敗を確認
    result = check_game()

    if result == "win":
        show_map(island, players, treasures, exit_position)
        print("おめでとう！ゲームクリア！")
        break

    elif result == "lose":
        show_map(island, players, treasures, exit_position)
        print("ゲームオーバー！")
        break

    # 次のプレイヤーへ交代
    turn = (turn + 1) % 2


print("\nゲームを終了します")

