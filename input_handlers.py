from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        keys = {
            tcod.event.K_UP: MovementAction(dx=0,dy=-1),
            tcod.event.K_DOWN: MovementAction(dx=0, dy=1),
            tcod.event.K_LEFT: MovementAction(dx=-1, dy=0),
            tcod.event.K_RIGHT: MovementAction(dx=1, dy=0),
            tcod.event.K_y: MovementAction(dx=-1, dy=-1),
            tcod.event.K_u: MovementAction(dx=1, dy=-1),
            tcod.event.K_b: MovementAction(dx=-1, dy=1),
            tcod.event.K_n: MovementAction(dx=1, dy=1),
            tcod.event.K_ESCAPE: EscapeAction(),
        }

        if key in keys:
            action = keys.get(key)

        # No valid key was pressed
        return action