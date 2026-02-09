const buttons = document.querySelectorAll(".hero-actions button");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    if (button.classList.contains("primary")) {
      window.location.href = "mailto:lorem@ipsum.com";
      window.location.href = "mailto:hello@mattkwade.com";
      return;
    }

    document.querySelector("#story").scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  });
});
