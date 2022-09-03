function initSurvey() {
    const resultSurvey = {
        R: 0,
        T: 0,
        C: 0,
        F: 0,
        J: 0,
        M: 0,
        A: 0,
        N: 0
    }

    return resultSurvey
}

function getScoreBoard(surveyElement) {
    const type1 = surveyElement[0]
    const type2 = surveyElement[1]

    const surveyBoard = {
        1: [type1, 3],
        2: [type1, 2],
        3: [type1, 1],
        4: 0,
        5: [type2, 1],
        6: [type2, 2],
        7: [type2, 3]
    }

    return surveyBoard
}

function getPersonalResult(resultSurvey) {
    const types = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]

    let answer = ""
    for(let[a, b] of types) {
        aScore = resultSurvey[a]
        bScore = resultSurvey[b]
        if(aScore === bScore) {
            answer += a
        } else if(aScore > bScore) {
            answer += a
        } else {
            answer += b
        }
    }

    return answer
}

function solution(survey, choices) {
    const resultSurvey = initSurvey()

    for (let i = 0; i < survey.length;  i++) {
        const scoreBoard = getScoreBoard(survey[i])
        if(choices[i] !== 4) {
            const[personalType, score] = scoreBoard[choices[i]]
            resultSurvey[personalType] += score
        }
    }

    const answer = getPersonalResult(resultSurvey)

    return answer
}
