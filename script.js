const buttons = document.querySelectorAll(".hero-actions button");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    if (button.classList.contains("primary")) {
      window.location.href = "mailto:hello@mattkwade.com";
      return;
    }

    // Rely on CSS smooth scrolling, native jump to anchor
    window.location.hash = "story";
  });
});

// Intersection Observer for scroll animations
const observerOptions = {
  root: null,
  rootMargin: "0px",
  threshold: 0.15,
};

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("active");
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll(".reveal").forEach((element) => {
  observer.observe(element);
});
