import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 380
    height: 640
    visible: true
    title: qsTr("Hello World")
    Rectangle{
        color: 'lightgrey'
        width: parent.width * 0.85
        height: parent.height * 0.9
        anchors.centerIn: parent



        Rectangle{
            id: rect_red
            color: 'red'
            width: 100
            height: 100
            anchors.bottom: rect_yellow.top
            anchors.bottomMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter
        }
        Rectangle{
            id: rect_yellow
            color: 'yellow'
            width: 100
            height: 100
            anchors.centerIn: parent
        }
        Rectangle{
            id: rect_green
            color: 'green'
            width: 100
            height: 100
            anchors.top: rect_yellow.bottom
            anchors.topMargin: 10
            anchors.horizontalCenter: parent.horizontalCenter

        }
        states:[
            State {
                name: "stop"
                when: mouseArea.pressed
                PropertyChanges {
                    target: rect_red
                    color: "red"
                }
                PropertyChanges {target:rect_yellow; color: "grey"}
                PropertyChanges {target:rect_green; color: "grey"}
            },
            State {
                name: "caution"
                when: mouseArea.pressed
                PropertyChanges {target: rect_red; color: "grey"}
                PropertyChanges {target:rect_yellow; color: "yellow"}
                PropertyChanges {target:rect_green; color: "grey"}
            },
            State {
                name: "go"
                when: mouseArea.pressed
                PropertyChanges {target: rect_red; color: "grey"; }
                PropertyChanges {target:rect_yellow; color: "grey"}
                PropertyChanges {target:rect_green; color: "green"}
            } ]
        state:"stop"
        MouseArea{
            anchors.fill:parent
            onClicked: {
                if (parent.state === "stop") {
                    parent.state = "caution";
                } else if (parent.state === "caution") {
                    parent.state = "go";
                } else {
                    parent.state = "stop";
                }
            }
        }
        transitions:[
            Transition {
                from: "stop"
                to: "caution"
                PropertyAnimation{
                 target:rect_red; property: "color"
                 duration: 500}},
            Transition {
                from: "caution"
                to: "go"
                PropertyAnimation{
                 target:rect_yellow; property: "color"
                 duration: 500}},
            Transition {
                from: "go"
                to: "stop"
                PropertyAnimation{
                 target:rect_green; property: "color"
                 duration: 500}}
        ]
    }
}
