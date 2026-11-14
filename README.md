# tiny-chess-01 entry

A chess engine in 4,077 bytes of Python (stdlib only), built for the
make.fun "Build the strongest chess engine in 4 KB of Python" bounty.

How it plays: it talks to the trial env over HTTP (`POST /game`, `/move`),
parses the FEN into a 0x88 board, and picks a move with iterative-deepening
negamax alpha-beta plus a captures-only quiescence search, under a fixed
node budget (never a clock, so replays match move for move). Move ordering
is MVV-LVA with a promotion bonus; the evaluation is material plus small
formula-based positional terms (pawn advancement, piece centrality, rook
on the 7th rank).

Move generation is verified by perft against the five standard positions
(startpos, kiwipete, and the three tricky ones with promotions, castling
and en passant).

Practice result (local trial vs the house gauntlet, trial0c): Elo 1173
(1 win, 3 draws, 4 losses) — drew vs depth-2, depth-4 and nodes-1M,
won vs depth-3 as black. Known weakness: the evaluation overvalues pawn
pushes in the opening.

Entry: `main.py` (the whole engine). License: MIT.
