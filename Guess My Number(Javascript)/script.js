'use strict';

// console.log(document.querySelector('.message').textContent);
// document.querySelector('.message').textContent = 'Correct Number!🎉';

let num = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highscore = 0;

// function for displaying message
const displayMessage = message => {
  document.querySelector('.message').textContent = message;
};

const reset = function () {
  score = 20;
  num = Math.trunc(Math.random() * 20) + 1;
  document.querySelector('.number').textContent = '?';
  document.querySelector('body').style.backgroundColor = '#222';
  displayMessage('Start guessing...');
  displayScore(score);
  document.querySelector('.guess').value = '';
};

// function for displaying score
const displayScore = score => {
  document.querySelector('.score').textContent = score;
};

// for testing purposes
//document.querySelector('.number').textContent = num;

document.querySelector('.check').addEventListener('click', function () {
  //console.log(document.querySelector('.guess').value); // shows in console , doesnt affect the page
  const guess = document.querySelector('.guess').value;

  console.log(guess, typeof guess); // test

  if (score <= 0) {
    document.querySelector('.number').textContent = num;
    displayMessage('You lost the game👎');
    return;
  }

  if (guess < 1 || guess > 20) {
    displayMessage('Invalid Input');
  } else if (guess == num) {
    displayMessage('Correct Number!🎉');
    highscore = Math.max(highscore, score);
    document.querySelector('.highscore').textContent = highscore;
    document.querySelector('.number').textContent = num;
    displayScore(score);
    document.querySelector('body').style.backgroundColor = '#60b347';
  } else {
    if (guess < num - 2) {
      displayMessage('Too low');
      score--;
      displayScore(score);
      return;
    }

    if (guess > num + 2) {
      displayMessage('Too high');
      score--;
      displayScore(score);
      return;
    }

    if (guess < num && num - guess <= 2) {
      displayMessage('Low but close');
      score--;
      displayScore(score);
      return;
    }

    if (guess > num && guess - num <= 2) {
      displayMessage('High but close');
      score--;
      displayScore(score);
    }
  }
});

document.querySelector('.again').addEventListener('click', function () {
  console.log('Again button clicked');
  reset();
});
