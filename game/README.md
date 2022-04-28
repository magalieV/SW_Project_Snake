<h1>Create elements</h1>

To create the snake and the apple you need to pass the screen and screen size as parameters.


> Snake(screen, screen_size)

> Apple(screen_size, screen)

<hr>

<h1> Update</h1>

> snake.update()

This handle the snake moving (not from the input of the user).
It needs to be placed before the events collide.

<hr>

<h1>Events</h1>

> snake.event_trigger(event)

This function will move the snake according to the user input.

> snake_collide(screen_size, apple)

This function will handle the collision between the map borders and the apple.

<hr>

<h1>Display</h1>

> apple.display()

> snake.display()

These functions simply display the sprite on the board.