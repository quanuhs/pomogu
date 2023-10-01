import { sleep } from 'k6'
import http from 'k6/http'

export const options = {
  stages: [
    { duration: '1m', target: 10 }, // Равномерное увеличение нагрузки до 10 пользователей в течение 1 минуты
    { duration: '3m', target: 10 }, // Поддержание нагрузки 10 пользователей в течение 3 минут
    { duration: '1m', target: 50 }, // Равномерное увеличение нагрузки до 50 пользователей в течение 1 минуты
    { duration: '3m', target: 50 }, // Поддержание нагрузки 50 пользователей в течение 3 минут
    { duration: '1m', target: 100 }, // Равномерное увеличение нагрузки до 100 пользователей в течение 1 минуты
    { duration: '3m', target: 100 }, // Поддержание нагрузки 100 пользователей в течение 3 минут
    { duration: '1m', target: 50 }, // Уменьшение нагрузки до 50 пользователей в течение 1 минуты
    { duration: '3m', target: 50 }, // Поддержание нагрузки 50 пользователей в течение 3 минут
    { duration: '1m', target: 10 }, // Уменьшение нагрузки до 10 пользователей в течение 1 минуты
    { duration: '3m', target: 10 }, // Поддержание нагрузки 10 пользователей в течение 3 минут

  ],
  thresholds: {
    http_req_failed: ['rate<0.02'], // http ошибок должно быть меньше 2%
    http_req_duration: ['p(95)<2000'], // 95% запросов должны быть меньше 2s
  },
  ext: {
    loadimpact: {
      distribution: {
        frankfurtDistribution: {loadZone: 'amazon:de:frankfurt', percent: 100},


      },
      projectID: 3644606,
      name: 'pomogu'
    },
  },
}

export default function main() {
  let response = http.get('https://pomogu.su/', {
    headers: {
      Accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    },
  });
  sleep(1);
}