export function getDateFromDatetime(date) {
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ];
    let newDate = new Date(date)
    return monthNames[newDate.getMonth()] + " " + newDate.getMonth().toString()
}

export function randomMinRead(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}