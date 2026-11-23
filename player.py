from map import SIZE, SUNK


# -------------------------
# エンジニアの移動処理
# -------------------------
def move_engineer(player, direction, island):

    row = player["position"][0]
    col = player["position"][1]

    # 移動方向を決定
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

    # マップの範囲を確認
    if 0 <= row < SIZE and 0 <= col < SIZE:

        # 沈んでいないマスなら移動
        if island[row][col] != SUNK:
            player["position"] = [row, col]
            return True

        else:
            print("そのマスには移動できません")
            return False

    else:
        print("マップの範囲外です")
        return False


# -------------------------
# パイロットの移動処理
# -------------------------
def move_pilot(player, row, col, island):

    # マップの範囲を確認
    if 0 <= row < SIZE and 0 <= col < SIZE:

        # 沈んでいないマスなら移動
        if island[row][col] != SUNK:
            player["position"] = [row, col]
            return True

        else:
            print("そのマスには移動できません")
            return False

    else:
        print("マップの範囲外です")
        return False
