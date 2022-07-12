--[[
    ScoreState Class
    Author: Colton Ogden
    cogden@cs50.harvard.edu

    A simple state used to display the player's score before they
    transition back into the play state. Transitioned to from the
    PlayState when they collide with a Pipe.
]]

ScoreState = Class{__includes = BaseState}

--[[
    When we enter the score state, we expect to receive the score
    from the play state so we know what to render to the State.
]]
function ScoreState:enter(params)
    self.score = params.score

    -- # TODO - Add Trophies -- Put inside functions input score output image (?)
    if self.score >= 5 then
        -- Render Gold Image
        self.medal = love.graphics.newImage('gold_medal.png')
        print("Won the Gold Medal!")
    elseif self.score <= 4 and self.score >= 3 then
        -- Render Silver Image
        self.medal = love.graphics.newImage('silver_medal.png')
        print("Won the Silver Medal!")
    elseif self.score <= 2 and self.score >= 1 then
        -- Render Bronze Image
        self.medal = love.graphics.newImage('bronze_medal.png')
        print("Won the Bronze Medal!")
    else
        print("No trophy :(")
    end

    self.x = VIRTUAL_WIDTH - 220
    self.y = 100

end

function ScoreState:update(dt)
    -- go back to play if enter is pressed
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        print("Restart")
        gStateMachine:change('countdown')
    end
end

function ScoreState:render()
    -- simply render the score to the middle of the screen
    love.graphics.setFont(flappyFont)
    love.graphics.printf('Oof! You lost!', 0, 64, VIRTUAL_WIDTH, 'center')

    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 100, VIRTUAL_WIDTH, 'center')

    -- # TODO - Draw Trophy
    if self.score >= 2 then
        love.graphics.draw(self.medal, self.x, self.y, 0, 0.1, 0.1)
    end

    love.graphics.printf('Press Enter to Play Again!', 0, 160, VIRTUAL_WIDTH, 'center')
end