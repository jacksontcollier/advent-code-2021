#!/usr/bin/env python3

import day13
import origami_paper

positions, fold_positions = day13.parse_input('test_input.txt')
paper = origami_paper.OrigamiPaper(positions, fold_positions)
paper.print_original_state()

