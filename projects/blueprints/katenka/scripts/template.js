'use strict';

const pageTemplate = 
  `
    <div id="main">
      <header>

        <h1
            id="title"
            class="header__title"
          >
          {{ lang ? "Фан Катёнки" : "Fan of Katenka" }}
        </h1>

        <button
            class="header__language-button"
            @click="changeLang"
          >
          {{ lang ? "English version" : "Русская версия" }}
        </button>

        <div class="header__logo">
          <img src="images/favicon.ico" />
        </div>

        <div 
            class="header__description"
            align="center"
          >
          {{ lang ? "Визуальная новелла" : "A visual novel" }}
        </div>

      </header>


      <div class="content">
        <div class="content__head">

          <div
              id="img-div"
              class="content__image-wrapper"
              align="center"
            >

            <figure>

              <img 
                  id="image"
                  class="content__main-image"
                  src="images/katenkavk.jpg"
                  alt="Your's God"
                />
              
              <figcaption
                  id="img-caption"
                  class="content__image-caption"
                >
                {{ lang ? "Твой Бог" : "Your's God" }}
              </figcaption>

            </figure>

          </div>


          <div
              id="tribute-info"
              class="content__info"
            >

              <p>
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
                asdaaaaaaaaaaaaaaaaaaaaaaaa
                adssssssssssssssssssssssss
                dasssssssssssssssssssssssss
              </p>

          </div>

        </div>

        <div class="content__stories">

        </div>
      </div>


      <footer>

        <a
            id="tribute-link"
            class="footer__link"
            href="https://vk.com/katenkafelix"
            target="_blank"
          >
          {{ lang ? "Катёнка Феликс" : "Katenka Felix" }}
        </a>

        <span class="footer__copyright">
          {{ lang ? "Себя защити" : "Copyright yourself" }}, 2018
        </span>

      </footer>

    </div>
  `;