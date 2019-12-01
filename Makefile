DAY := $(shell date "+%d")

day:
	mkdir -p $(DAY)
	open https://adventofcode.com/2019/day/$(DAY)

.PHONY: day
