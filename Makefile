DAY := $(shell date "+%d")
TIMMED_DAY := $(shell date "+%-d")
day:
	mkdir -p $(DAY)
	open https://adventofcode.com/2019/day/$(TIMMED_DAY)

.PHONY: day
