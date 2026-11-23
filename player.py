from map import SIZE, SUNK


# -------------------------
# プレイヤーの初期設定
# -------------------------
def create_players():

    players = [
        {
            "name": "エンジニア",
            "role": "engineer",
            "position": [0, 0],
            "actions": 3,
            "special_used": False
        },
        {
            "name": "パイロット",
            "role": "pilot",
            "position": [3, 3],
            "actions": 3,
            "special_used": False
        }
    ]

    return players


# -------------------------
# エンジニアの移動
# -------------------------
def move_engineer(player, direction, island):

    # アクション数を確認
    if player["actions"] <= 0:
        print("アクションが残っていません")
        return False

    row = player["position"][0]
    col = player["position"][1]

    # 移動方向
    if direction == "w":
        row -= 1
    elif direction == "s":
        row += 1
    elif direction == "a":
        col -= 1
    elif direction == "d":
        col += 1
    else:
        print("入力が正しくありません")
        return False

    # マップの範囲確認
    if 0 <= row < SIZE and 0 <= col < SIZE:

        # 沈没していないマスなら移動
        if island[row][col] != SUNK:

            player["position"] = [row, col]
            player["actions"] -= 1

            return True

        else:
            print("そのマスには移動できません")
            return False

    else:
        print("マップの範囲外です")
        return False


# -------------------------
# パイロットの移動
# -------------------------
def move_pilot(player, row, col, island):

    # アクション数を確認
    if player["actions"] <= 0:
        print("アクションが残っていません")
        return False

    # マップの範囲確認
    if not (0 <= row < SIZE and 0 <= col < SIZE):
        print("マップの範囲外です")
        return False

    # 沈没マスには移動できない
    if island[row][col] == SUNK:
        print("そのマスには移動できません")
        return False

    current_row = player["position"][0]
    current_col = player["position"][1]

    # 移動先が現在地と同じ場合
    if current_row == row and current_col == col:
        print("現在いるマスです")
        return False

    # 隣接しているか確認
    distance = abs(current_row - row) + abs(current_col - col)

    # 隣接マスへの通常移動
    if distance == 1:

        player["position"] = [row, col]
        player["actions"] -= 1

        return True

    # 特殊能力による自由移動
    else:

        if player["special_used"]:
            print("特殊能力はこのターン使用済みです")
            return False

        player["position"] = [row, col]
        player["actions"] -= 1
        player["special_used"] = True

        return True


# -------------------------
# ターン開始処理
# -------------------------
def start_turn(player):

    player["actions"] = 3
    player["special_used"] = False
