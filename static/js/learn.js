function main_section_attach() {
  const learnBtn = document.getElementById("btn-learn-selected");
  const checkBtns = document.querySelectorAll('input[id^="check-single-"]');
  const check_all_btn = document.getElementById("check-all");
  const reinputs = document.querySelectorAll('input[id^="input-"]');
  const select = document.getElementById("add-to-tab");
  const tabBtns = document.querySelectorAll('button[id^="tab-"]');
  const addTabBtn = document.getElementById("btn-add-tab");
  const addTabInput = document.getElementById("input-add-tab");
  const addWordBtn = document.getElementById("btn-add-word");
  const inputWord = document.getElementById("add-word-input-word");
  const inputPinyin = document.getElementById("add-word-input-pinyin");
  const inputMeaning = document.getElementById("add-word-input-meaning");
  const shuffle = document.getElementById("shuffle");
  const tbody = document.getElementsByTagName("tbody")[0];

  const shuffler = (array) => { 
    return array.sort(() => Math.random() - 0.5); 
  }; 

  if (shuffle != null) {
    shuffle.addEventListener("click", () => {
      rows = Array.from(document.querySelectorAll("tr[id^='word-row-']"));
      var shuffled = shuffler(rows);
      var i = 1;
      shuffled.forEach((trow) => {
        trow.children[0].innerText = i;
        i++;
        tbody.appendChild(trow);
      });

    });
  }

  if (reinputs != null) {
    reinputs.forEach((input) => {
      input.addEventListener("input", () => {
        const word =
          input.parentElement.parentElement.querySelector(
            'td[id^="word-"]'
          ).textContent;
        const meaning =
          input.parentElement.parentElement.querySelector('td[id^="meaning-"]');
        if (input.value == word) {
          meaning.style.display = "table-cell";
        }
      });
    });
  }

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

  if (check_all_btn != null) {
    check_all_btn.addEventListener("change", () => {
      checkBtns.forEach((button) => {
        button.checked = check_all_btn.checked;
      });
      learnBtn.disabled = !check_all_btn.checked;
    });
  }

  if (checkBtns != null) {
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
  }

  if (learnBtn != null) {
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

  if (select != null) {
    select.addEventListener("change", (event) => {
      let tab_id = event.target.value;
      console.log("tab_id", tab_id);
      let word_ids = [];
      checkBtns.forEach((button) => {
        if (button.checked) {
          word_ids.push(button.value);
        }
      });

      fetch("/tab/add_word", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ tab_id, word_ids }),
      })
        .then((response) => {
          if (!response.ok) {
            console.log("Tag: error to add word to tab");
          }
          return response.text();
        })
        .then((text) => {
          alert(text);
        });
    });
  }

  if (tabBtns != null) {
    tabBtns.forEach((button) => {
      button.addEventListener("click", () => {
        tab_id = button.value;
        fetch("/tab/get_words", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ tab_id }),
        })
          .then((response) => {
            if (!response.ok) {
              console.log("Tag: error to fetch words");
            }
            return response.text();
          })
          .then((html) => {
            document.getElementById("main-section").innerHTML = html;
            main_section_attach();
          });
      });
    });
  }

  if (addWordBtn != null) {
    addWordBtn.addEventListener("click", () => {
      word = inputWord.value.trim();
      meaning = inputMeaning.value.trim();
      pinyin = inputPinyin.value.trim();
      if (word.length > 0 && meaning.length > 0) {
        fetch("/word/add", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ word, pinyin, meaning }),
        })
          .then((response) => {
            if (!response.ok) {
              console.log("Word: failed to add word");
            }
            return response.text();
          })
          .then((html) => {
            document.getElementById("main-section").innerHTML = html;
            main_section_attach();
          });
      }
    });
  }

  if (addTabBtn != null) {
    addTabBtn.addEventListener("click", () => {
      tab_name = addTabInput.value.trim();
      if (tab_name.length > 0) {
        fetch("/tab/add", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ tab_name }),
        })
          .then((response) => {
            if (!response.ok) {
              console.log("Tab: failed to add tab");
            }
            return response.text();
          })
          .then((html) => {
            document.getElementById("tab-section").innerHTML = html;
            main_section_attach();
          });
      }
    });
  }
}

main_section_attach();
