
# 財宝を回収する関数
def collect_treasure(player, treasures):

    position = player["position"]

    # 財宝があるか確認
    if position in treasures:

        treasures.remove(position.copy())

        print("財宝を回収しました！")
        return True

    else:
        print("このマスには財宝がありません")
        return False

