from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GeneralBattleAssets: 


	# Click Rule Assets
	# description 
	C_WIN_1 = RuleClick(roi_front=(175,102,1054,99), roi_back=(175,102,1054,99), name="win_1")
	# description 
	C_WIN_2 = RuleClick(roi_front=(22,112,210,496), roi_back=(22,112,210,496), name="win_2")
	# description 
	C_WIN_3 = RuleClick(roi_front=(1059,114,206,468), roi_back=(1059,114,206,468), name="win_3")
	# description 
	C_REWARD_1 = RuleClick(roi_front=(606,603,325,87), roi_back=(606,603,325,87), name="reward_1")
	# description 
	C_REWARD_2 = RuleClick(roi_front=(25,134,224,472), roi_back=(25,134,224,472), name="reward_2")
	# description 
	C_REWARD_3 = RuleClick(roi_front=(1092,156,168,437), roi_back=(1092,156,168,437), name="reward_3")


	# Click Rule Assets
	# 预设队伍1 
	C_PRESET_TEAM_1 = RuleClick(roi_front=(195,235,465,110), roi_back=(195,235,465,110), name="preset_team_1")
	# 预设队伍2 
	C_PRESET_TEAM_2 = RuleClick(roi_front=(195,355,465,110), roi_back=(195,355,465,110), name="preset_team_2")
	# 预设队伍3 
	C_PRESET_TEAM_3 = RuleClick(roi_front=(195,475,465,110), roi_back=(195,475,465,110), name="preset_team_3")
	# 预设队伍4 
	C_PRESET_TEAM_4 = RuleClick(roi_front=(195,595,465,35), roi_back=(195,595,465,35), name="preset_team_4")
	# 预设组1 
	C_PRESET_GROUP_1 = RuleClick(roi_front=(35,240,25,50), roi_back=(35,240,25,50), name="preset_group_1")
	# 预设组2 
	C_PRESET_GROUP_2 = RuleClick(roi_front=(35,305,25,50), roi_back=(35,305,25,50), name="preset_group_2")
	# 预设组3 
	C_PRESET_GROUP_3 = RuleClick(roi_front=(35,365,25,50), roi_back=(35,365,25,50), name="preset_group_3")
	# 预设组4 
	C_PRESET_GROUP_4 = RuleClick(roi_front=(35,430,25,50), roi_back=(35,430,25,50), name="preset_group_4")
	# 预设组5 
	C_PRESET_GROUP_5 = RuleClick(roi_front=(35,495,25,50), roi_back=(35,495,25,50), name="preset_group_5")
	# 预设组6 
	C_PRESET_GROUP_6 = RuleClick(roi_front=(35,555,25,50), roi_back=(35,555,25,50), name="preset_group_6")
	# 预设组7 
	C_PRESET_GROUP_7 = RuleClick(roi_front=(35,615,25,50), roi_back=(35,615,25,50), name="preset_group_7")
	# 从左开始第一个绿标 
	C_GREEN_LEFT_1 = RuleClick(roi_front=(128,433,90,150), roi_back=(128,433,90,150), name="green_left_1")
	# 从左开始第二个绿标 
	C_GREEN_LEFT_2 = RuleClick(roi_front=(371,385,81,145), roi_back=(371,385,81,145), name="green_left_2")
	# 从左开始第三个绿标 
	C_GREEN_LEFT_3 = RuleClick(roi_front=(586,328,100,76), roi_back=(586,328,100,76), name="green_left_3")
	# 从左开始第四个绿标 
	C_GREEN_LEFT_4 = RuleClick(roi_front=(817,379,77,133), roi_back=(817,379,77,133), name="green_left_4")
	# 从左开始第五个绿标 
	C_GREEN_LEFT_5 = RuleClick(roi_front=(1059,416,85,145), roi_back=(1059,416,85,145), name="green_left_5")
	# 绿标阴阳师 
	C_GREEN_MAIN = RuleClick(roi_front=(590,454,88,178), roi_back=(590,454,88,178), name="green_main")
	# 绿标点击 区域,默认为全屏，需要在代码中更新其区域 
	C_GREEN_MARK_AREA = RuleClick(roi_front=(0,0,1280,720), roi_back=(0,0,1280,720), name="green_mark_area")
	# 战斗的时候有一定的概率随机点击 
	C_RANDOM_CLICK = RuleClick(roi_front=(104,79,1050,507), roi_back=(255,65,100,100), name="random_click")


	# Image Rule Assets
	# 奖励，就是那个魂 
	I_REWARD = RuleImage(roi_front=(547,518,172,96), roi_back=(547,518,172,96), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward.png")
	# 预设的小图标 
	I_PRESET = RuleImage(roi_front=(32,650,47,45), roi_back=(32,650,47,45), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_preset.png")
	# 准备 
	I_PREPARE_HIGHLIGHT = RuleImage(roi_front=(1128,536,100,100), roi_back=(1110,500,169,200), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_prepare_highlight.png")
	# 战斗胜利 
	I_WIN = RuleImage(roi_front=(385,47,100,100), roi_back=(296,33,414,224), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_win.png")
	# 准备但是界面还未加载这个时候是黑色的 
	I_PREPARE_DARK = RuleImage(roi_front=(1131,538,100,100), roi_back=(1131,538,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_prepare_dark.png")
	# 失败 
	I_FALSE = RuleImage(roi_front=(413,124,100,100), roi_back=(413,124,100,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_false.png")
	# 确认预设的队伍 
	I_PRESET_ENSURE = RuleImage(roi_front=(352,643,141,50), roi_back=(305,625,236,83), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_preset_ensure.png")
	# 选择buff 
	I_BUFF = RuleImage(roi_front=(115,670,39,36), roi_back=(107,668,55,49), threshold=0.7, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff.png")
	# 觉醒加成 
	I_BUFF_AWAKEN = RuleImage(roi_front=(373,126,383,53), roi_back=(373,126,383,53), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_awaken.png")
	# 御魂加成 
	I_BUFF_SOUL = RuleImage(roi_front=(377,192,371,56), roi_back=(377,192,371,56), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_soul.png")
	# 金币加成50 
	I_BUFF_GOLD_50 = RuleImage(roi_front=(375,259,373,56), roi_back=(375,259,373,56), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_gold_50.png")
	# 金币加成100 
	I_BUFF_GOLD_100 = RuleImage(roi_front=(371,329,389,54), roi_back=(371,329,389,54), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_gold_100.png")
	# 经验加成50 
	I_BUFF_EXP_50 = RuleImage(roi_front=(378,400,370,50), roi_back=(378,400,370,50), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_exp_50.png")
	# 经验加成100 
	I_BUFF_EXP_100 = RuleImage(roi_front=(372,463,386,50), roi_back=(372,463,386,50), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_buff_exp_100.png")
	# 左下角的位置指针 
	I_LOCAL = RuleImage(roi_front=(25,563,30,34), roi_back=(25,563,30,34), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_local.png")
	# description 
	I_STATISTICS = RuleImage(roi_front=(61,644,33,28), roi_back=(61,644,33,28), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_statistics.png")
	# 左上角的退出 
	I_EXIT = RuleImage(roi_front=(14,12,43,41), roi_back=(14,12,43,41), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_exit.png")
	# 退出确认 
	I_EXIT_ENSURE = RuleImage(roi_front=(674,388,135,63), roi_back=(674,388,135,63), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_exit_ensure.png")
	# 左上角好友图标 
	I_FRIENDS = RuleImage(roi_front=(89,14,36,36), roi_back=(89,14,36,36), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_friends.png")
	# 结算时左下角统计图标 
	I_REWARD_STATISTICS = RuleImage(roi_front=(51,629,54,59), roi_back=(51,629,54,59), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_statistics.png")
	# 结算金币 
	I_REWARD_GOLD = RuleImage(roi_front=(268,178,97,69), roi_back=(254,163,797,261), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_gold.png")
	# 结算紫蛇皮 
	I_REWARD_PURPLE_SNAKE_SKIN = RuleImage(roi_front=(604,213,67,37), roi_back=(108,163,1070,261), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_purple_snake_skin.png")
	# 结算金蛇皮 
	I_REWARD_GOLD_SNAKE_SKIN = RuleImage(roi_front=(537,176,97,75), roi_back=(254,163,797,261), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_gold_snake_skin.png")
	# 结算四星青吉鬼 
	I_REWARD_EXP_SOUL_4 = RuleImage(roi_front=(806,177,97,69), roi_back=(254,163,797,261), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_exp_soul_4.png")
	# 结算五星御魂 
	I_REWARD_SOUL_5 = RuleImage(roi_front=(266,533,97,20), roi_back=(254,163,797,396), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_soul_5.png")
	# 结算六星御魂 
	I_REWARD_SOUL_6 = RuleImage(roi_front=(942,397,97,20), roi_back=(254,163,797,396), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_reward_soul_6.png")
	# 针对封魔的特殊 
	I_DE_WIN = RuleImage(roi_front=(472,49,100,100), roi_back=(239,36,399,133), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_de_win.png")
	# description 
	I_PRESENT_LESS_THAN_5 = RuleImage(roi_front=(222,648,418,43), roi_back=(222,648,418,43), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_present_less_than_5.png")
	# 封魔的金币 
	I_DE_GOLD = RuleImage(roi_front=(61,52,30,25), roi_back=(45,33,65,64), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_de_gold.png")
	# 绿标 
	I_GREEN_MARKER = RuleImage(roi_front=(0,0,1280,720), roi_back=(0,0,1280,720), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_green_marker.png")
	# 绿标-左上角部分 
	I_GREEN_MARKER_LEFT_TOP = RuleImage(roi_front=(0,0,1280,720), roi_back=(0,0,1280,720), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_green_marker_left_top.png")
	# 绿标-下半部分 
	I_GREEN_MARKER_BOTTOM = RuleImage(roi_front=(0,0,1280,720), roi_back=(0,0,1280,720), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_green_marker_bottom.png")
	# 新版本的预设图案带数字 
	I_PRESET_WIT_NUMBER = RuleImage(roi_front=(40,655,37,37), roi_back=(9,636,100,74), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_preset_wit_number.png")


	# Image Rule Assets
	# description 
	I_GREED_GHOST = RuleImage(roi_front=(56,40,45,45), roi_back=(56,40,45,45), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralBattle/gb/gb_greed_ghost.png")


	# Ocr Rule Assets
	# 准备 
	O_BATTLE_PREPARE = RuleOcr(roi=(1122,546,92,51), area=(1122,546,92,51), mode="Single", method="Default", keyword="准备", name="battle_prepare")
	# 预设,部分场景预设按钮上的文字为'预设'+数字,导致点击preset失败 
	O_PRESET = RuleOcr(roi=(20,620,60,80), area=(20,620,60,80), mode="Single", method="Default", keyword="预", name="preset")


	# Swipe Rule Assets
	# description 
	S_BATTLE_RANDOM_LEFT = RuleSwipe(roi_front=(122,155,480,426), roi_back=(667,147,461,427), mode="default", name="battle_random_left")
	# description 
	S_BATTLE_RANDOM_RIGHT = RuleSwipe(roi_front=(719,138,417,392), roi_back=(237,163,387,394), mode="default", name="battle_random_right")


