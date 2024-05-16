function main_section_attach() {
  const learnBtn = document.getElementById("btn-learn-selected");
  const checkBtns = document.querySelectorAll('input[id^="check-single-"]');
  const check_all_btn = document.getElementById("check-all");
  const reinputs = document.querySelectorAll('input[id^="input-"]');

  reinputs.forEach(input => {
    input.addEventListener('input', () => {
        const word = input.parentElement.parentElement.querySelector('td[id^="word-"]').textContent;
        const meaning = input.parentElement.parentElement.querySelector('td[id^="meaning-"]');
        if (input.value == word) {
            meaning.style.display = "table-cell";
        }
    })
  })


  function switch_learnBtn() {
    let disabled = 0;
    checkBtns.forEach((button) => {
      if (!button.checked) {
        disabled++;
        check_all_btn.checked = false;
      }
    });
    if (disabled === checkBtns.length) {
      return true;
    }
    return false;
  }

  check_all_btn.addEventListener("change", () => {
    checkBtns.forEach((button) => {
      button.checked = check_all_btn.checked;
    });
    learnBtn.disabled = !check_all_btn.checked;
  });

  checkBtns.forEach((button) => {
    button.addEventListener("change", () => {
      if (button.checked) {
        console.log("enabled");
        learnBtn.disabled = !button.checked;
      } else {
        console.log("disabled");
        learnBtn.disabled = switch_learnBtn();
      }
    });
  });

  learnBtn.addEventListener("click", () => {
    let word_ids = [];
    checkBtns.forEach((button) => {
      if (button.checked) {
        word_ids.push(button.value);
      }
    });

    fetch("/learn", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(word_ids),
    })
      .then((response) => {
        if (!response.ok) {
          console.log("Learn: failed to get words to learn");
        }
        return response.text();
      })
      .then((html) => {
        document.getElementById("main-section").innerHTML = html;
        main_section_attach();
      });
  });
}

main_section_attach();
