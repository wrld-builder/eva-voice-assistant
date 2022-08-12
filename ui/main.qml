import QtQuick 2.12
import QtQuick.Window 2.12

Window {
    id: window
    width: 70
    height: 70
    visible: true
    opacity: 0.6
    flags: Qt.FramelessWindowHint
    x: Screen.width / 2
    y: 5

    Rectangle {
        id: rectangle
        width: 60
        height: 60
        color: "skyblue"
        anchors.centerIn: parent
        border.width: 4
        radius: 2

        Rectangle {
            id: rotating_rectangle
            width: 15
            height: 15
            color: "blue"
            anchors.centerIn: parent

            RotationAnimation on rotation {
                from: 0
                to: 360
                duration: 1500
                running: true
            }
        }

        Rectangle {
            id: moving_rectangle
            width: 10
            height: 10
            color: "darkgreen"
            x: parent.left
            y: parent.bottom
            radius: 2
        }
    }

    SequentialAnimation {
        running: true

        NumberAnimation {
            target: moving_rectangle
            properties: "x"
            from: moving_rectangle.x
            to: moving_rectangle.x + 50
            duration: 500
        }

        NumberAnimation {
            target: moving_rectangle
            properties: "y"
            from: moving_rectangle.y
            to: moving_rectangle.y + 50
            duration: 500
        }

        NumberAnimation {
            target: moving_rectangle
            properties: "x"
            from: moving_rectangle.x + 50
            to: moving_rectangle.x - 50
            duration: 500
        }
    }

    Timer {
        interval: 3000
        onTriggered: Qt.quit()
        running: true
    }
}
