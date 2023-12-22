from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class MetaDemonAssets: 


	# Image Rule Assets
	# description 
	I_MD_ENTER = RuleImage(roi_front=(426,463,60,80), roi_back=(239,369,547,215), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_enter.png")
	# description 
	I_MD_MAIN = RuleImage(roi_front=(658,156,41,139), roi_back=(636,133,100,245), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_main.png")
	# description 
	I_MD_FIND = RuleImage(roi_front=(1112,581,100,100), roi_back=(1112,581,100,100), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_find.png")
	# 高 
	I_MD_HARD = RuleImage(roi_front=(513,515,26,27), roi_back=(513,515,26,27), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_hard.png")
	# description 
	I_MD_FIRE = RuleImage(roi_front=(1107,563,109,113), roi_back=(1107,563,109,113), threshold=0.7, method="Template matching", file="./tasks/MetaDemon/md/md_md_fire.png")
	# description 
	I_MD_GIFT_BOX = RuleImage(roi_front=(1184,182,42,50), roi_back=(1184,182,42,50), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_gift_box.png")
	# 难度 
	I_MD_EXTREME = RuleImage(roi_front=(512,516,30,25), roi_back=(512,516,30,25), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_extreme.png")
	# description 
	I_MD_FIRE_COMMON = RuleImage(roi_front=(1065,499,100,36), roi_back=(1065,499,100,36), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_fire_common.png")
	# description 
	I_MD_FIRE_POWER = RuleImage(roi_front=(1159,498,100,37), roi_back=(1159,498,100,37), threshold=0.8, method="Template matching", file="./tasks/MetaDemon/md/md_md_fire_power.png")


	# Ocr Rule Assets
	# Ocr-description 
	O_MD_EXHAUSTION = RuleOcr(roi=(1096,18,89,31), area=(1096,18,89,31), mode="DigitCounter", method="Default", keyword="", name="md_exhaustion")
	# Ocr-description 
	O_MD_TICKET = RuleOcr(roi=(923,18,82,30), area=(923,18,82,30), mode="DigitCounter", method="Default", keyword="", name="md_ticket")


