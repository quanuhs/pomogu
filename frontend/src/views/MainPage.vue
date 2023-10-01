<script setup lang="ts">
    import { defineAsyncComponent } from 'vue';
    import { getMyProfile } from '../api'

    const ImageIntro = defineAsyncComponent(() => import('../components/icons/ImageIntro.vue'))
</script>

<template>
    
    <div class="content">
        <main class="main">
            <div class="into">
                <h1 class="headline">Онлайн-терапия</h1>
                <div class="text">
                    Мы предоставляем онлайн-терапию, основанную на научных и этических стандартах. Наша команда лучших
                    психологов использует передовые методики работы для решения ваших жизненных проблем. Вы можете
                    получить квалифицированную помощь прямо из уюта своего дома, в безопасном и комфортном пространстве.
                    Наша цель - помочь вам решить любые вызовы, с которыми вы сталкиваетесь в жизни.
                </div>

                <div class="btn-group bold">
                    <a class="btn btn-primary" href="/search">Найти помощь</a>
                    <a class="btn btn-secondary" href="/me">Помочь</a>
                </div>
            </div>

            <div class="image">
              <ImageIntro/>
            </div>
        </main>

        <div class="info">
            <div class="info-text">
                <h2>Занимайтесь в любом месте</h2>
                <div class="text">Мы опираемся на научные данные и придерживаемся жестких этических правил. Отбираем
                    лучших
                    психологов и внедряем передовые методики работы.

                </div>
            </div>
            <div class="info-image">
                <img width="220" height="100%" alt="pasta" src="/landing_info_1_compressed.webp">
                <img width="115" height="130" alt="coffee" src="/landing_info_2_compressed.webp">

            </div>
        </div>
    
    </div>
</template>

<script lang="ts">

// getMyProfile()


</script>

<style>

.text{
    text-align: justify;
}

.into{
    min-height: 300px;
    max-width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: stretch;
    
    gap: 30px;
}

.headline{
    text-align: left;
}

.image{
    max-width: 100%;
    min-width: 50%;
    height: auto;
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;

}

.main{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

.btn-group > a{
    text-align: center;
    outline: none;
    text-decoration: none;
    color: #000000;
    flex: 2 1 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 44px;
    
    transition: 0.3s;

}

.btn-group > a:hover{
    box-shadow: 1px 1px 5px 2px rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}

.info{
    max-height: 250px;
    margin-top: 100px;
    display: flex;
    justify-content: space-evenly;
    flex-direction: row;
    background: #FFFFFF;
    border-radius: 10px;
}

.info-text{
    margin: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
/*     max-width: 300px; */
}

.info-image > img{
    pointer-events: none;
    user-select: none;

}

.info-image{
    display: flex;
    justify-content: flex-end;
    align-items: center;

    overflow: hidden;

    margin-left: auto;
    max-width: 30%;

    
    clip-path: polygon(2% 0%, 90% 300%,100% 100%, 100% 0%);
    border-radius: 10px;
    width: 100%;
    background-color: hsl(34, 53%, 82%);
    background-image: repeating-linear-gradient(45deg, transparent 5px, hsla(197, 62%, 11%, 0.5) 5px, hsla(197, 62%, 11%, 0.5) 10px,
  hsla(5, 53%, 63%, 0) 10px, hsla(5, 53%, 63%, 0) 35px, hsla(5, 53%, 63%, 0.5) 35px, hsla(5, 53%, 63%, 0.5) 40px,
  hsla(197, 62%, 11%, 0.5) 40px, hsla(197, 62%, 11%, 0.5) 50px, hsla(197, 62%, 11%, 0) 50px, hsla(197, 62%, 11%, 0) 60px,
  hsla(5, 53%, 63%, 0.5) 60px, hsla(5, 53%, 63%, 0.5) 70px, hsla(35, 91%, 65%, 0.5) 70px, hsla(35, 91%, 65%, 0.5) 80px,
  hsla(35, 91%, 65%, 0) 80px, hsla(35, 91%, 65%, 0) 90px, hsla(5, 53%, 63%, 0.5) 90px, hsla(5, 53%, 63%, 0.5) 110px,
  hsla(5, 53%, 63%, 0) 110px, hsla(5, 53%, 63%, 0) 120px, hsla(197, 62%, 11%, 0.5) 120px, hsla(197, 62%, 11%, 0.5) 140px
  ),
repeating-linear-gradient(135deg, transparent 5px, hsla(197, 62%, 11%, 0.5) 5px, hsla(197, 62%, 11%, 0.5) 10px,
  hsla(5, 53%, 63%, 0) 10px, hsla(5, 53%, 63%, 0) 35px, hsla(5, 53%, 63%, 0.5) 35px, hsla(5, 53%, 63%, 0.5) 40px,
  hsla(197, 62%, 11%, 0.5) 40px, hsla(197, 62%, 11%, 0.5) 50px, hsla(197, 62%, 11%, 0) 50px, hsla(197, 62%, 11%, 0) 60px,
  hsla(5, 53%, 63%, 0.5) 60px, hsla(5, 53%, 63%, 0.5) 70px, hsla(35, 91%, 65%, 0.5) 70px, hsla(35, 91%, 65%, 0.5) 80px,
  hsla(35, 91%, 65%, 0) 80px, hsla(35, 91%, 65%, 0) 90px, hsla(5, 53%, 63%, 0.5) 90px, hsla(5, 53%, 63%, 0.5) 110px,
  hsla(5, 53%, 63%, 0) 110px, hsla(5, 53%, 63%, 0) 140px, hsla(197, 62%, 11%, 0.5) 140px, hsla(197, 62%, 11%, 0.5) 160px
);
}


@media all and (max-width: 830px){
    .main{
        flex-direction: column;
        padding: 0 5% 0 5%
    }

    .headline{
        text-align: center;

        font-size: 24px;
        line-height: 29px;
    }


    .info{
        flex-direction: column;
        max-height: 500px;
    }


    .info-image{
        border-top-left-radius: 0;
        border-top-right-radius: 0;
        clip-path: polygon(0% 0%, 100% 100000%, 0% 100%, 100000% 100%);
        max-height: 200px;
        justify-content: center;
        margin-left: 0;
        max-width: 100%;

    }

    .image{
        margin-top: 25px;
    }

    .image > svg{
        max-width: 550px;
    }

    
}

</style>
