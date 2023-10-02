// Click events for buttons
const portfolio = document.getElementById("portfolio");
const portfolioBtn = document.getElementById("portfolio-btn");
const skills = document.getElementById("skills");
const skillsBtn = document.getElementById("skills-btn");

portfolioBtn.addEventListener("click", (event) => {
  skills.style.display = "none";
  portfolio.style.display = "flex";
  skillsBtn.classList.remove("active-btn");
  portfolioBtn.classList.add("active-btn");
});

skillsBtn.addEventListener("click", (event) => {
  skills.style.display = "flex";
  portfolio.style.display = "none";
  portfolioBtn.classList.remove("active-btn");
  skillsBtn.classList.add("active-btn");
});

// Light & Dark Theme
document.addEventListener("DOMContentLoaded", () => {
  const toggleThemeButton = document.getElementById("toggleTheme");
  const themeIcon = document.querySelector('img[alt="theme icon"]');
  const githubLogo = document.querySelector('img[alt="github logo"]');
  const linkedinLogo = document.querySelector('img[alt="linkedin logo"]');
  const instaLogo = document.querySelector('img[alt="insta logo"]');
  const youtubeLogo = document.querySelector('img[alt="youtube logo"]');

  const lightLogos = {
    github: "static/core/images/github_light.png",
    linkedin: "static/core/images/linkedin_light.png",
    insta: "static/core/images/insta_light.png",
    youtube: "static/core/images/youtube_light.png",
    theme:"static/core/images/theme_light.png",
  };

  const darkLogos = {
    github: "static/core/images/github_dark.png",
    linkedin: "static/core/images/linkedin_dark.png",
    insta: "static/core/images/insta_dark.png",
    youtube: "static/core/images/youtube_dark.png",
    theme: "static/core/images/theme_dark.png",
  };

  function setTheme(isDark) {
    githubLogo.src = isDark ? darkLogos.github : lightLogos.github;
    linkedinLogo.src = isDark ? darkLogos.linkedin : lightLogos.linkedin;
    instaLogo.src = isDark ? darkLogos.insta : lightLogos.insta;
    youtubeLogo.src = isDark ? darkLogos.youtube : lightLogos.youtube;
    themeIcon.src = isDark ? darkLogos.theme : lightLogos.theme;
  }

  toggleThemeButton.addEventListener("click", () => {
    const isDark = document.body.classList.toggle("dark-theme");
    localStorage.setItem("isDark", isDark);

    setTheme(isDark);
  });

  const loadTheme = () => {
    const isDark = localStorage.getItem("isDark") === "true";
    document.body.classList.toggle("dark-theme", isDark);

    setTheme(isDark);
  };

  // Load saved theme from local storage or default to light theme
  loadTheme();
});